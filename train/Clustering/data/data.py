import csv
import mysql.connector

# MySQL database connection configuration
db_config = {
    "host": "localhost",
    "user": "glsa",
    "password": "1234",
    "database": "glsa"
}

# Open the CSV file and insert the data into the MySQL table
def insert_data_from_csv(file_path):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)  # Skip the header row of the CSV file
            for row in csv_reader:
                ID, Prompt, SUM, MEM_change, Time_seconds, isSeq, Model = row
                query = "INSERT INTO profileseq (ID, Prompt, SUM, MEM_change, Time_seconds, isSeq, Model) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                values = (ID, Prompt, SUM, MEM_change, Time_seconds, isSeq, Model)
                cursor.execute(query, values)

        connection.commit()
        print("Data inserted successfully!")

    except mysql.connector.Error as error:
        print("Data insertion failed:", error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Specify the CSV file path and call the function to insert data
csv_file_path = '/path/to/data'  # Replace with your CSV file path
insert_data_from_csv(csv_file_path)
