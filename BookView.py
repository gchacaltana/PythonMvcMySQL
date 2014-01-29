# -*- coding: utf-8 *-*
__author__ = 'Gonzalo Chacaltana Buleje'
import sys

class BookView:

    def __init__(self):
        self.tab1 = "    "
        self.tab2 = "    " * 2
        self.tab3 = "    " * 3
        self.txt_opt = "%sSeleccione: " % self.tab2
        self.txt_category = "%sCategoria: " % self.tab3
        self.txt_title = "%sTítulo: " % self.tab3
        self.txt_price = "%sPrecio: " % self.tab3
        self.txt_id = "%sLibro ID: " % self.tab3
        pass

    def show_main(self):
        """show main view"""

        options = """
        Seleccione una opción:
            (1) Agregar libro
            (2) Listar libros
            (3) Editar un libro
            (4) Eliminar un libro
            (0) Salir

        """

        print options

        choose = raw_input(self.txt_opt)
        return choose

    def create_book(self):
        """view of the form to create new book"""

        print """
        Nuevo Libro
        """
        category = raw_input(self.txt_category)
        title = raw_input(self.txt_title)
        price = raw_input(self.txt_price)
        return (category, title, price)

    def show_message_created(self):
        """return message created book"""

        print """
        Libro creado con éxito!
        """

    def list_books(self, list_book):

        print """
        Listado de Libros:
        """

        for row in list_book:
            id = row[0]
            category = row[1]
            title = row[2]
            print("%s[%d] %s (%s)" % (self.tab3, id, category, title))