import itertools
import sqlite3
import json

# List of steps
steps = [
    "0", "1.1", "1.2", "1.3", "2.1", "2.2", "3.1", "3.2", "3.3", "3.4", "3.5",
    "3.6", "4.1", "4.2", "4.3", "4.4", "5.1", "5.2", "5.3", "5.4", "5.5",
    "6.1", "6.2", "6.3", "6.4"
]

# Generate all combinations
combinations = itertools.product(["False", "True"], repeat=len(steps))

# Connect to SQLite database
conn = sqlite3.connect('effios.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS Combinaisons (ID INTEGER PRIMARY KEY, Combination TEXT)''')

# Insert combinations into the table
for idx, combination in enumerate(combinations, start=1):
    combination_dict = {step: state for step, state in zip(steps, combination)}
    combination_json = json.dumps(combination_dict)
    cursor.execute("INSERT INTO Combinaisons (ID, Combination) VALUES (?, ?)", (idx, combination_json))
    #print(f"Inserted row {idx}: {combination_dict}")

print("Combinations inserted successfully into the 'Combinaisons' table.")

conn.commit()
conn.close()
