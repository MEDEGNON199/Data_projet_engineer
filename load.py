import pandas as pd
from sqlalchemy import create_engine, text

# Connexion PostgreSQL
engine = create_engine(
    "postgresql://postgres:0000@localhost:5432/data_engineer_db"
)

with engine.begin() as conn:
    # Vider les tables dans le bon ordre
    conn.execute(text("DELETE FROM tasks"))
    conn.execute(text("DELETE FROM users"))
    conn.execute(text("DELETE FROM projects"))

# Lire les données
df = pd.read_json("data/tasks.json")
df["created_at"] = pd.to_datetime(df["created_at"])

# USERS
users = df[["user"]].drop_duplicates().reset_index(drop=True)
users.columns = ["name"]
users.to_sql("users", engine, if_exists="append", index=False)

# PROJECTS
projects = df[["project"]].drop_duplicates().reset_index(drop=True)
projects.columns = ["name"]
projects.to_sql("projects", engine, if_exists="append", index=False)

# Récupérer IDs
users_db = pd.read_sql("SELECT * FROM users", engine)
projects_db = pd.read_sql("SELECT * FROM projects", engine)

df = df.merge(users_db, left_on="user", right_on="name")
df = df.merge(projects_db, left_on="project", right_on="name")

# TASKS
tasks = df[[
    "task_id",
    "title",
    "status",
    "priority",
    "id_x",
    "id_y",
    "created_at"
]]

tasks.columns = [
    "id",
    "title",
    "status",
    "priority",
    "user_id",
    "project_id",
    "created_at"
]

tasks.to_sql("tasks", engine, if_exists="append", index=False)

print("Données chargées avec succès")
