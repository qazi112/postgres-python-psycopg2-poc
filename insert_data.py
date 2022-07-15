from asyncio import constants
from return_connection import getConnection, closeConnection


def insertData():
    # Get the connection
    connection = getConnection()

    # Get the cursor
    cursor = connection.cursor()

    # INSERT DATA
    # Sql query/command
    sql = """ INSERT INTO users (username)
        VALUES (%s) RETURNING *;
     """

    cursor.execute(sql, ("Arsalan Shah",))

    user_data = cursor.fetchone()
    print(user_data)
    connection.commit()
    # Close the connection
    closeConnection(connection)


if __name__ == "__main__":
    insertData()
