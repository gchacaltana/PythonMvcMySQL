# -*- coding: utf-8 *-*
__author__ = 'Gonzalo Chacaltana Buleje'
import MySQLdb


class MySQLConnection:

    db_hostname = "localhost"
    db_user = "root"
    db_password = "sistemas"
    db_database = "bookstore"
    connection = None
    cursor = None
    rows = None

    def __init__(self, hostname="", user="", password="", database=""):
        self.db_hostname = self.db_hostname if hostname == "" else hostname
        self.db_user = self.db_user if user == "" else user
        self.db_password = self.db_password if password == "" else password
        self.db_database = self.db_database if database == "" else database

    def connect(self):
        """MySQL connection Method"""
        self.connection = MySQLdb.connect(self.db_hostname, self.db_user, self.db_password, self.db_database);
        self.cursor = self.connection.cursor()

    def close(self):
        """close the connection to mysql"""
        self.cursor.close()

    def execute(self, query, values=''):
        """running sql statement"""
        self.connect()
        if values != '':
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)

    def get_fetch_rows(self):
        """returning data"""
        self.rows = self.cursor.fetchall()

    def commit(self, query):
        """commit sql statement"""
        sql = query.lower()
        if sql.count('select') < 1:
            self.connection.commit()