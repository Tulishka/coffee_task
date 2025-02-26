import sqlite3

DATA_COFFEE_SQLITE = "data/coffee.sqlite"


def save_coffee(coffee_id, ground_or_beans, name, package_volume, price, roast_level, taste_description) -> bool:
    try:
        con = sqlite3.connect(DATA_COFFEE_SQLITE)
        cur = con.cursor()

        if coffee_id:
            cur.execute("""
                UPDATE coffee SET
                name=?, roast_level=?, ground_or_beans=?, taste_description=?, price=?, package_volume=?
                WHERE id=?
            """, (name, roast_level, ground_or_beans, taste_description, price, package_volume, coffee_id))
        else:
            cur.execute("""
                INSERT INTO coffee (name, roast_level, ground_or_beans, taste_description, price, package_volume)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (name, roast_level, ground_or_beans, taste_description, price, package_volume))

        con.commit()
        con.close()
        return True
    except sqlite3.Error as e:
        print(f"Ошибка: {e}")

    return False


def get_coffee(coffee_id):
    res = None
    try:
        con = sqlite3.connect(DATA_COFFEE_SQLITE)
        cur = con.cursor()
        cur.execute("SELECT * FROM coffee WHERE id=?", (coffee_id,))
        res = cur.fetchone()
        con.close()
    except sqlite3.Error as e:
        print(f"Ошибка: {e}")
    return res


def get_coffee_list():
    rows = []
    try:
        con = sqlite3.connect(DATA_COFFEE_SQLITE)
        cur = con.cursor()
        cur.execute("SELECT * FROM coffee")
        rows = cur.fetchall()
        con.close()
    except sqlite3.Error as e:
        print(f"Ошибка: {e}")
    return rows
