import sqlite3

conn = sqlite3.connect("corona_data.db")
cursor = conn.cursor()


def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS basic_details (
         id integer PRIMARY KEY,
         first_name text NOT NULL,
         last_name text NOT NULL,
         address text,
         birth_date date,
         phone text)""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS covid_details (
                             id integet PRIMARY KEY,
                             vaccination_date date,
                             vaccination_factory text,
                             positive_date date,
                             FOREIGN KEY(id) REFERENCES basic_details(id))""")


def insert_basic_data(u_id, u_first_name, u_last_name, u_address, u_birth_date, u_phone):
    cursor.execute("""INSERT INTO basic_details (id, first_name, last_name, address, birth_date, phone) VALUES
                    (?, ?, ?, ?, ?, ?)""", (u_id, u_first_name, u_last_name, u_address, u_birth_date, u_phone))


def insert_vaccination_data(u_id, u_vaccination_date, u_vaccination_factory, u_positive_date):
    cursor.execute("""INSERT INTO covid_details (id, vaccination_date, vaccination_factory, positive_date) VALUES
                    (?, ?, ?, ?)""", (u_id, u_vaccination_date, u_vaccination_factory, u_positive_date))


def retrieval(u_id, table_name):
    cursor.execute("""SELECT * FROM ? WHERE id = ?""", (table_name, u_id))


def my_execute(sql_query):
    cursor.execute(sql_query)


conn.commit()
conn.close()







# Create a connection to the database
# def get_db():
#     conn = sqlite3.connect("details.db")
#     cursor = conn.cursor()
#     # conn.text_factory = sqlite3.Row
#     return conn.cursor()
#
#
# def create_db():
#     data_base = get_db()
#     create_basic = '''CREATE TABLE IF NOT EXISTS basic_details (id integer PRIMARY KEY,
#     first_name text NOT NULL,
#     last_name text NOT NULL,
#     address text,
#     birth_date text,
#     phone text)'''
#     data_base.execute(create_basic)
#     # Create table for COVID-19 related details
#     create_corona = '''CREATE TABLE IF NOT EXISTS covid_details (
#                         id integet PRIMARY KEY,
#                         patient_id integer,
#                         vaccination_date text,
#                         vaccination_factory text,
#                         positive_corona_date text,
#                         FOREIGN KEY(patient_id) REFERENCES basic_details(id))'''
#     data_base.execute(create_corona)

# def close_db():
#     # Commit changes and close connection
#     conn.commit()
#     conn.close()
