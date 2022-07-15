import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()

print(os.getenv("DATABASE"))


def getConnection():
    try:
        connection = psycopg2.connect(
            database=os.getenv("DATABASE"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            host=os.getenv("HOST")
        )
        print(connection)
        return connection

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def closeConnection(connection):
    try:
        connection.close()
        print("Connection Closed")
        print(connection)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


if __name__ == "__main__":
    connection = getConnection()
    closeConnection(connection)
