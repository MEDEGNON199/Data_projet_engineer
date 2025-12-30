import pandas as pd

# Lire les données
df = pd.read_json("data/tasks.json")

# Nettoyage des textes
df["title"] = df["title"].str.strip()
df["project"] = df["project"].str.strip()
df["user"] = df["user"].str.strip()

# Normaliser les statuts
status_mapping = {
    "done": "DONE",
    "in_progress": "IN_PROGRESS",
    "todo": "TODO"
}
df["status"] = df["status"].map(status_mapping)

# Convertir la date
df["created_at"] = pd.to_datetime(df["created_at"])

# Vérification finale
print(df)
print(df.dtypes)
