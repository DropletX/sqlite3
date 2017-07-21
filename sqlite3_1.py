import sqlite3

class Database:
    def __init__(self,db):
        """
        Connect to database or create a database if not exists.
        db: database file name.
        """
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()

    def __del__(self):
        """
        Close connection to database.
        """
        self.conn.close()

    def dbcommit(self):
        """
        Write changes to database.
        """
        self.conn.commit()
