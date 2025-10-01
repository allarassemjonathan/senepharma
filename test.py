import csv
import json

# Fichier CSV d'entrée
csv_file = "senepharma.csv"

# Fichier JSON de sortie
json_file = "medicaments.json"

# Dictionnaire final
data = {}

# Lecture du CSV
with open(csv_file, newline='', encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row["name"].strip()
        price = f'{row["price"]} FCFA'
        description = name.title()  # rend la première lettre de chaque mot majuscule

        data[name] = {
            "price": price,
            "description": description
        }

# Écriture dans un fichier JSON
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"✅ Fichier JSON généré: {json_file}")
