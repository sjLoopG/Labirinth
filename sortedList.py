# Beispiel-Daten
daten = [
    {"name": "Alice", "zeit": 35.2},
    {"name": "Bob", "zeit": 42.0},
    {"name": "Charlie", "zeit": 38.5},
    {"name": "David", "zeit": 31.8},
    {"name": "Eve", "zeit": 40.6}
]

# Liste nach Zeit sortieren
sortierte_liste = sorted(daten, key=lambda x: x["zeit"])

# Ausgabe der sortierten Liste
for eintrag in sortierte_liste:
    print("Name:", eintrag["name"], "- Zeit:", eintrag["zeit"])