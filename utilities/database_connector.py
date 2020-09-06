import mysql.connector
from mysql.connector import errorcode

class DatabaseConnector():
    __connection = None
    __session = None

    def open(self):
        try:
            db_connector = mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                passwd="root",
                database="pythondbtest"
            )
            self.__connection = db_connector
            self.__session = db_connector.cursor()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('Something is wrong with your user name or password')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print('Database does not exists')
            else:
                print(err)

    def close(self):
        self.__session.close()
        self.__connection.close()

    def run_non_select(self, query):
        self.open()
        self.__session.execute(query)
        self.__connection.commit()
        self.close()
        return self.__session.lastrowid

    def run_select(self, query):
        results = None
        self.open()
        self.__session.execute(query)
        results = self.__session.fetchall()
        self.close()
        return results
