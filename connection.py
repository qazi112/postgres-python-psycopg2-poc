import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("HOST"),
      os.getenv("USER"),
      os.getenv("DATABASE"),
      os.getenv("PASSWORD"))


def connect():
    try:
        connection = psycopg2.connect(
            database=os.getenv("DATABASE"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            host=os.getenv("HOST")
        )

        # Got the cursor
        cursor = connection.cursor()

        # Get the Postgres version
        cursor.execute("SELECT version()")
        db_version = cursor.fetchone()
        print(db_version)

        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print("Database Connection Closed!")


if __name__ == "__main__":
    connect()
