# -*- coding: utf-8 *-*
__author__ = 'Gonzalo Chacaltana Buleje'


class BookView:

    def __init__(self):
        self.tab1 = "    "
        self.tab2 = "    " * 2
        self.tab3 = "    " * 3
        self.txt_opt = "%sChoose: " % self.tab2
        self.txt_category = "%sCategory: " % self.tab3
        self.txt_title = "%sTitle: " % self.tab3
        self.txt_price = "%sPrice: " % self.tab3
        self.txt_id = "%sBook ID: " % self.tab3
        pass

    def show_main(self):
        """show main view"""

        options = """
        Select a menu option:
            (1) Add Book
            (2) List Books
            (3) Edit a Book
            (4) Delete a Book
            (0) Logout

        """

        print options

        choose = raw_input(self.txt_opt)
        return choose

    def create_book(self):
        """view of the form to create new book"""

        print """
        CREATE A NEW BOOK
        """
        category = raw_input(self.txt_category)
        title = raw_input(self.txt_title)
        price = raw_input(self.txt_price)
        return (category, title, price)

    def show_message_created(self):
        """return message created book"""

        print """
        Book successfully created!
        """