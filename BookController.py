# -*- coding: utf-8 *-*
__author__ = 'Gonzalo Chacaltana Buleje'
from  Book import Book
from BookView import BookView


class BookController:

    def __init__(self):
        self.view = BookView()
        self.book_main_controller()

    def book_main_controller(self):
        """main method controller"""
        request = self.view.show_main()
        self.request = int(request)

        if self.request == 1:
            self.create_book()
        elif self.request == 2:
            self.list_books()
        elif self.request == 3:
            self.edit_book()
        elif self.request == 4:
            self.delete_book()

    def create_book(self):
        """create book"""
        (category, title, price) = self.view.create_book()
        objBook = Book()
        objBook.id_category = category
        objBook.title = title
        objBook.price = price
        objBook.create()

        self.view.show_message_created()
        self.book_main_controller()

controller = BookController()