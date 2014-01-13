# -*- coding: utf-8 *-*
__author__ = 'Gonzalo Chacaltana Buleje'
from MySQLConnection import MySQLConnection


class Book:

    def __init__(self):
        self.id_book = 0
        self.id_category = ''
        self.title = ''
        self.price = ''
        self.date_created = 'NOW()'
        self.db = MySQLConnection()

    def create(self):
        """create a new record"""
        query = "INSERT INTO books (id_book, id_category,name,price,date_created) values (null, %s, %s, %s, NOW())"
        values = (self.id_category, self.title, self.price)
        self.db.execute(query, values)
        self.db.commit(query)