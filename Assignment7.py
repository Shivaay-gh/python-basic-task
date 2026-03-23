import psycopg2

# connect to database
def get_connection():
    return psycopg2.connect(
        dbname="testdb",
        user="postgres",
        password="12345678",
        host="localhost",
        port="5432"
    )

# create table
def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS students (id SERIAL PRIMARY KEY, name VARCHAR(50), age INT);""")
    conn.commit()
    cur.close()
    conn.close()


# insert data
def insert_data():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("INSERT INTO students (name, age) VALUES (%s, %s);", ('Shivaay', 20))
    conn.commit()
    cur.close()
    conn.close()


# fetch data
def fetch_data():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM students;")
    rows = cur.fetchall()

    print("\nStudent Records:")
    for row in rows:
        print(row)

    cur.close()
    conn.close()

# main execution
if __name__ == "__main__":
    create_table()
    insert_data()
    fetch_data()
