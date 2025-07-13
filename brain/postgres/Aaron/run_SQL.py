import psycopg2
import os

## Connect to database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="P0stgres",
    host="localhost",
    port="5432"
)
# cursor
crsr = conn.cursor()

# run SQL scripts
def run_sql_scripts(sql_file_path):
    with open(sql_file_path, "r") as file:
        sql_command = file.read()
    crsr.execute(sql_command)
    conn.commit()
def display_data(table_name):
    crsr.execute(f"SELECT * FROM {table_name};")
    rows = crsr.fetchall()  # fetch all rows
    for row in rows:
        print(row)

## DDL
sql_create_path = "C:/Users/dokiu/OneDrive/Documents/Coding Practice/ai-at-dscubed-forked/brain/postgres/Aaron/DDL/create_data_schema.sql"

## DML
sql_insert_path = "C:/Users/dokiu/OneDrive/Documents/Coding Practice/ai-at-dscubed-forked/brain/postgres/Aaron/DML/insert_into_table.sql"

## Run SQL scripts
run_sql_scripts(sql_create_path)
run_sql_scripts(sql_insert_path)

## Display data
display_data("project_two.spotify_top_artists")

## Close the connection
conn.close()