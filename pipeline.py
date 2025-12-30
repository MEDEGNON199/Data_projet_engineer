import subprocess

print("=== DÉMARRAGE DU PIPELINE ===")

print("1️⃣ Extraction des données")
subprocess.run(["py", "extract.py"], check=True)

print("2️⃣ Transformation des données")
subprocess.run(["py", "transform.py"], check=True)

print("3️⃣ Chargement des données")
subprocess.run(["py", "load.py"], check=True)

print("=== PIPELINE TERMINÉ AVEC SUCCÈS ===")
