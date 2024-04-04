import sqlite3
import json

# Connect to SQLite database
conn = sqlite3.connect('effios.db')
cursor = conn.cursor()

# Retrieve all combinations from the Combinaisons table
cursor.execute("SELECT ID, Combination FROM Combinaisons")
combinations = cursor.fetchall()

# Retrieve all rules from the Regles table
cursor.execute("SELECT ID, Regle FROM Regles")
rules = cursor.fetchall()

# Create table correspondance_combinaison_regle
cursor.execute('''CREATE TABLE IF NOT EXISTS correspondance_combinaison_regle (ID INTEGER PRIMARY KEY, CombinaisonID INTEGER, RegleID INTEGER)''')

# Function to evaluate the rule against the combination
def evaluate_rule(rule, combination_data):
    rule = rule.replace("0", "combination_data['0']")
    rule = rule.replace("1.1", "combination_data['1.1']")
    rule = rule.replace("1.2", "combination_data['1.2']")
    rule = rule.replace("1.3", "combination_data['1.3']")
    rule = rule.replace("2.1", "combination_data['2.1']")
    rule = rule.replace("2.2", "combination_data['2.2']")
    rule = rule.replace("3.1", "combination_data['3.1']")
    rule = rule.replace("3.2", "combination_data['3.2']")
    rule = rule.replace("3.3", "combination_data['3.3']")
    rule = rule.replace("3.4", "combination_data['3.4']")
    rule = rule.replace("3.5", "combination_data['3.5']")
    rule = rule.replace("3.6", "combination_data['3.6']")
    rule = rule.replace("4.1", "combination_data['4.1']")
    rule = rule.replace("4.2", "combination_data['4.2']")
    rule = rule.replace("4.3", "combination_data['4.3']")
    rule = rule.replace("4.4", "combination_data['4.4']")
    rule = rule.replace("5.1", "combination_data['5.1']")
    rule = rule.replace("5.2", "combination_data['5.2']")
    rule = rule.replace("5.3", "combination_data['5.3']")
    rule = rule.replace("5.4", "combination_data['5.4']")
    rule = rule.replace("5.5", "combination_data['5.5']")
    rule = rule.replace("6.1", "combination_data['6.1']")
    rule = rule.replace("6.2", "combination_data['6.2']")
    rule = rule.replace("6.3", "combination_data['6.3']")
    rule = rule.replace("6.4", "combination_data['6.4']")
    # Evaluate the final expression
    return eval(rule)

# For each combination and rule, check if the combination satisfies the rule
for comb_id, comb_str in combinations:
    combination_data = json.loads(comb_str)
    for rule_id, rule_str in rules:
        # Evaluate the rule against the combination
        if evaluate_rule(rule_str, combination_data):
            print(f"Combination ID {comb_id} matches Rule ID {rule_id}.")
            cursor.execute("INSERT INTO correspondance_combinaison_regle (CombinaisonID, RegleID) VALUES (?, ?)", (comb_id, rule_id))

# Commit changes and close the connection
conn.commit()
conn.close()

print("Correspondances inserted successfully into the 'correspondance_combinaison_regle' table.")
