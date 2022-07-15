from return_connection import getConnection, closeConnection


def queryData():
    connection = getConnection()
    cursor = connection.cursor()

    sql = "SELECT * FROM users;"
    cursor.execute(sql)

    data = cursor.fetchone()
    print(type(data))
    print(data)
    closeConnection(connection)


if __name__ == "__main__":
    queryData()
