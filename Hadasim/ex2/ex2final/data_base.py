import sqlite3

# Define the database file location
DATABASE = 'HMO_data.db'


# Function to get a database connection and cursor
def get_cursor():
    conn = sqlite3.connect(DATABASE)
    conn.text_factory = sqlite3.Row
    return conn.cursor(), conn


# Function to close the database connection
def close_connection(conn):
    conn.commit()
    conn.close()


# Function to create the required tables: basic_details and covid details
def create_table():
    cursor, conn = get_cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS basic_details (
                     id text PRIMARY KEY,
                     first_name text NOT NULL,
                     last_name text NOT NULL,
                     city text,
                     street text,
                     birth_date date,
                     phone text,
                     mobile text)""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS covid_details (
                     id text,
                     vaccination_date date,
                     vaccination_factory text,
                     positive_date date,
                     recovery_date date,
                     PRIMARY KEY (id, vaccination_date),
                     FOREIGN KEY(id) REFERENCES basic_details(id))""")
    close_connection(conn)


# Function to insert the basic personal data of new client:
def insert_basic_data(u_id, u_first_name, u_last_name, u_city, u_street, u_birth_date, u_phone, u_mobile):
    cursor, conn = get_cursor()
    cursor.execute("""INSERT INTO basic_details (id, first_name, last_name, city, street, birth_date, phone, mobile) VALUES
                    (?, ?, ?, ?, ?, ?, ?, ?)""",
                   (u_id, u_first_name, u_last_name, u_city, u_street, u_birth_date, u_phone, u_mobile))
    close_connection(conn)


# Function to insert the vaccination data of a client:
def insert_covid_data(u_id, u_vaccination_date, u_vaccination_factory, u_positive_date, u_recovery_date):
    cursor, conn = get_cursor()
    cursor.execute("""INSERT INTO covid_details (id, vaccination_date, vaccination_factory, positive_date, recovery_date) VALUES
                    (?, ?, ?, ?, ?)""", (u_id, u_vaccination_date, u_vaccination_factory, u_positive_date, u_recovery_date))
    close_connection(conn)


# Function to retrieval data of specific client
def retrieval(u_id, table_name):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM {} WHERE id = ?""".format(table_name), (u_id,))
    result = cursor.fetchall()
    close_connection(conn)
    return result


# Function to execute any sql query by sqlite:
def exec(sql_query, parameters=()):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    rows = []
    try:
        cursor.execute(sql_query, parameters)
        rows = cursor.fetchall()
    except Exception as e:
        print("Error:", e)
        exit(0)
    finally:
        close_connection(conn)
        return rows


# Function to calculate the number of customers who are not vaccinated
def non_vaccination_sum():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    users_sum_sql = "SELECT id FROM basic_details"
    vaccinated_sum_sql = "SELECT id FROM covid_details GROUP BY id"
    users = exec(users_sum_sql)
    vaccinated = exec(vaccinated_sum_sql)
    return len(users) - len(vaccinated)
