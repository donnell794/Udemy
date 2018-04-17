import psycopg2

def connect():
    conn = psycopg2.connect("dbname='db1' user='postgres' password='donnell7' host='localhost' port='5432'")
    cur = conn.cursor()
    return conn, cur

def commit(conn):
    conn.commit()
    conn.close()

def create_table(db):
    conn, cur = connect()
    cur.execute("CREATE TABLE IF NOT EXISTS {} (item TEXT, quantity INTEGER, price REAL)".format(db))
    commit(conn)


def insert(db, item, quantity, price):
    conn, cur = connect()
    cur.execute("INSERT INTO {} VALUES (?,?,?)".format(db), (item, quantity, price))
    commit(conn)

def delete(db, item):
    conn, cur = connect()
    cur.execute("DELETE FROM {} WHERE item=?".format(db), (item,))
    commit(conn)

def update(db, quantity, item):
    conn, cur = connect()
    cur.execute("UPDATE {} SET quantity=? WHERE item=?".format(db),(quantity, item))
    commit(conn)

def view(db):
    conn, cur = connect()
    cur.execute("SELECT * FROM {}".format(db))
    rows = cur.fetchall()
    conn.close()
    return rows

def change_pass(user, new_pass):
    conn, cur = connect()
    cur.execute("ALTER USER {} WITH PASSWORD {};".format(user, new_pass))

create_table('store')
#insert('store','water glass', 10, 8)
#insert('store', 'coffe cup', 8, 5)
delete('store', 'coffe cup')
print(view('store'))
