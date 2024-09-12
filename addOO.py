import sqlite3
import _2x2Main as Main
import json
import shutil


def add_OO(old_state, new_state, rotation, alg):

    try:
        old_state = Main.invtranslDB(old_state)
        new_state = Main.invtranslDB(new_state)

        conn = sqlite3.connect('oo.db')
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM sqlite_master WHERE type = "table"''')
        tables = cursor.fetchall()

        for table in tables:
            cursor.execute(f"UPDATE {table[1]} SET state = ? WHERE state = ?", (new_state, old_state))
        cursor.execute("UPDATE solutionsTable SET oo = ? WHERE state = ?", (alg, new_state))
        cursor.execute(f'''SELECT solutions from solutionsTable WHERE state = "{new_state}"''')
        solutions_json = cursor.fetchone()
        solutions = json.loads(solutions_json[0])
        new_solutions = []
        for solution in solutions:
            new_solutions.append(Main.new_orientation(solution, rotation))
        new_solutions_json = json.dumps(new_solutions)
        cursor.execute("UPDATE solutionsTable SET solutions = ? WHERE state = ?", (new_solutions_json, new_state))

        conn.commit()

        cursor.execute("VACUUM")
        conn.close()

    except:
        print("State not found")


shutil.copy("oo.db", "oo_BACKUP.db")

with open("ADDOO.txt", 'r') as file:
    for line in file:
        parts = line.split('\t')
        add_OO(parts[0].strip(), parts[1].strip(), parts[2].strip(), parts[3].strip())
