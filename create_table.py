from return_connection import getConnection, closeConnection


def createTable():
    # Get the connection
    connection = getConnection()

    createTableQueries = [
        """
        CREATE TABLE users (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR (100) NOT NULL,
            created_at timestamp NOT NULL DEFAULT NOW()
        )
        """,
        """
        CREATE TABLE todos (
            todo_id SERIAL PRIMARY KEY,
            user_id INT NOT NULL,
            FOREIGN KEY (user_id)
            REFERENCES users (user_id)
            ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE tasks(
            task_id SERIAL PRIMARY KEY,
            todo_id INT NOT NULL,
            title VARCHAR(128) NOT NULL,
            description VARCHAR(1024) NOT NULL,
            FOREIGN KEY (todo_id) 
            REFERENCES todos (todo_id)
            ON UPDATE CASCADE ON DELETE CASCADE
        )
        """
    ]

    # Get the cursor
    cursor = connection.cursor()

    for query in createTableQueries:
        cursor.execute(query)

    cursor.close()
    connection.commit()
    closeConnection(connection)


createTable()
