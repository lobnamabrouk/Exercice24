import itertools
import sqlite3

# Define the rules for each status and sub-status
# Dictionary key:value
# ... replaced by True
rules = {
    "Information avant accrochage": "(0 or 1.1 or 1.2 or (1.1 and 1.2)) and not 1.3 and not 6.4",
    "En cours d'accrochage": "1.1 and 1.2 and 1.3 and not (2.1 and True and 5.5) and not 6.4",
    "En cours d'accrochage > Initialisation du projet d'accrochage": "1.1 and 1.2 and 1.3 and not 2.1 True not 5.5 and not 6.4",
    "En cours d'accrochage > Accrochage technique": "1.1 and 1.2 and 1.3 and 2.1 and 2.2 and not 5.5 and not 6.4",
    "En cours d'accrochage > Validation de conformité": "1.1 and 1.2 and 1.3 and 2.1 and 2.2 and 3.1 and 3.2 and 3.3 and 3.4 and 3.5 and not 5.5 and not 6.4",
    "En cours d'accrochage > Mise en production": "1.1 and True and 4.4 and not 5.1 True not 5.5 and not 6.4",
    "En production": "1.1 and True and 3.5 and 4.1 and 4.2 and 5.1 True and 5.5 and not 6.4",
    "En production - OK": "1.1 and True and 5.5 and not 6.4",
    "En production - Adaptations spécifiques": "1.1 and True and 3.5 and not 3.6 and 4.1 and True and 5.5 and not 6.4",
    "En production - Requalification CA": "1.1 and True and 3.5 and 4.1 and 4.2 and (not 4.3 or not 4.4 or (not 4.3 and not 4.4)) and 5.1 and True and 5.5 and not 6.4",
    "Accrochage stoppé": "6.4"
}

# Create table regles
cursor.execute('''CREATE TABLE IF NOT EXISTS Regles (ID INTEGER PRIMARY KEY, Statut TEXT, Regle TEXT)''')

# Insert rules into the table
for idx, (statut, regle) in enumerate(rules.items(), start=1):
    cursor.execute("INSERT INTO Regles (ID, Statut, Regle) VALUES (?, ?, ?)", (idx, statut, regle))

# Commit changes and close the connection
conn.commit()
conn.close()

print("Rules inserted successfully into the 'Regles' table.")
