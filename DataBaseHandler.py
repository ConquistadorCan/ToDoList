import sqlite3

class DataBaseHandler:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        self.createTable()

    def createTable(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS database (date TEXT, task TEXT)')
        self.conn.commit()

    def deleteData(self):
        self.cursor.execute('DELETE FROM database')

    def commit(self):
        self.conn.commit()

    def fetchAllItems(self):
        self.cursor.execute('SELECT * FROM database')
        return self.cursor.fetchall()

    def insertItem(self, date, task):
        self.cursor.execute('INSERT INTO database (date, task) VALUES (?, ?)',(date, task))
        self.conn.commit()

    def deleteItem(self, date, task):
        self.cursor.execute('DELETE FROM database WHERE date=? AND task=? ',(date, task))
        self.conn.commit()

    def clearTable(self):
        self.cursor.execute('DELETE FROM database;',)
        self.conn.commit()

    def closeConnection(self):
        self.conn.close()