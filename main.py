from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
            host="localhost",

            user=input("Enter username: "),
            password=getpass("Enter password: "),
            port=3306,
    ) as connection:
        print(connection)
except Error as e:
    print(e)
