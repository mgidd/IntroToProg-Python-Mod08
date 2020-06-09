# ------------------------------------------------------------------------ #
# Title: Assignment 8
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# MGiddings,5.6.2020,Modified code to complete portions of assignment 8
# MGiddings,5.7.2020,Modified code to complete more of assignment 8
# MGiddings,5.7.2020,Added more error handling & string formatting
# MGiddings,5.7.2020,Added commenting and supplemented docstrings
# ------------------------------------------------------------------------ #


# Data START ------------------------------------------------------------- #

# Declare variables
strFileName = 'products.txt'  # name of file
lstOfProductObjects = []  # list of objects


class Product:
    """Stores data about a product

    properties:
        product_name: (string) with the product's name
        product_price: (float) with the product's standard price
    methods:
        __str__: overrides built-in string to format objects
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created class
        MGiddings,6.7.2020,Added code to complete assignment 8
    """

    # -- Constructor -- #
    def __init__(self, product_name: str, product_price: float):
        # -- Attributes -- #
        self._product_name = product_name
        self._product_price = product_price

    # -- Properties -- #
    @property
    def product_name(self):
        return self._product_name.title()

    @product_name.setter
    def product_name(self, product_name):
        if not str(product_name).isnumeric():
            self._product_name = product_name
        else:
            raise Exception('Product name cannot contain numbers.')

    @property
    def product_price(self):
        return self._product_price

    @product_price.setter
    def product_price(self, product_price):
        if product_price.isnumeric():
            self._product_price = product_price
        else:
            raise Exception('Product price must be numbers.')

    # -- Methods -- #
    def __str__(self):
        return '{},${}'.format(self._product_name, self.product_price)

# Data END ---------------------------------------------------------------- #


# Processing START -------------------------------------------------------- #

class FileProcessor:
    """Processes data to and from a file and a list of product objects

    methods:
        read_data_from_file(file_name, list_of_objects): -> (a list of product objects)
        save_data_to_file(file_name, list_of_objects):

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        MGiddings,6.7.2020,Added code to complete assignment 8
    """

    # Added code to process data from a file
    @staticmethod
    def read_data_from_file(file_name, list_of_objects):
        """ Reads data from a file to a list of product objects

        :param file_name: (string) with name of file
        :param list_of_objects: (list) to add file data to
        :return: (list) of product objects
        """
        try:
            with open(file_name, 'r') as file:
                for row in file:
                    list_of_objects.append(row)
                file.close()
            return list_of_objects  # return list loaded from file
        except FileNotFoundError:
            print('\n' + 'File not found. Please try again.')

    # Added code to process data to a file
    @staticmethod
    def save_data_to_file(file_name, list_of_objects):
        """ Writes data from a list of product objects to a file

        :param file_name: (string) with name of file
        :param list_of_objects: (list) of data to save to file
        :return: nothing
        """
        with open(file_name, 'w') as file:
            for row in list_of_objects:
                file.write(str(row).strip() + '\n')  # writes data to file
            file.close()

# Processing END ---------------------------------------------------------- #


# Presentation (Input/Output) START --------------------------------------- #

class IO:
    # Added docstring to complete assignment 8
    """ Captures user input for menu choice, name and price
        Displays menu of choices and list of product objects

    methods:
        print_menu():
        input_menu_choice(): -> (menu choice)
        print_current_list(list_of_objects):
        input_name_and_price(): -> (object containing product name and price)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        MGiddings,6.7.2020,Added code to complete assignment 8
    """

    # Added code to show menu to user
    @staticmethod
    def print_menu():
        """ Displays a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu
        1 - Show current product list
        2 - Add product to list
        3 - Save product list to file and exit
        ''')

    # Added code to get user's menu choice
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from the user

        :return: (string) choice
        """
        choice = str(input('Which option would you like to perform? [1 to 3] - ')).strip()
        print()
        return choice

    # Added code to show current data from file to user
    @staticmethod
    def print_current_list(list_of_objects):
        """ Shows current data in the list of product objects

        :param list_of_objects: (list) of product objects
        :return: nothing
        """
        if list_of_objects == []:  # if empty list
            print('No products currently in list.')
        else:
            print('*** Product List ***')
            for row in list_of_objects:
                print(str(row).strip())

    # Added code to get product data from user
    @staticmethod
    def input_name_and_price():
        """ Gets product name and product price from the user

        :return: (object) of product name and price
        """
        obj_product = Product(product_name='', product_price=0)
        try:
            obj_product.product_name = str(input('Product name: '))
            obj_product.product_price = str(input('Product price: '))
        except Exception as e:
            print(e)
        return obj_product

# Presentation (Input/Output) END ----------------------------------------- #


# Main Body of Script START ----------------------------------------------- #

# Added code to main body to complete assignment 8

# Load data from file into a list of product objects when script starts
FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)

# Show user a menu of options
while True:
    IO.print_menu()

    # Get user's menu option choice
    strChoice = IO.input_menu_choice()

    # Show user current data in the list of product objects
    if strChoice.strip() == '1':
        IO.print_current_list(lstOfProductObjects)

    # Let user add data to the list of product objects
    elif strChoice.strip() == '2':
        objProduct = IO.input_name_and_price()
        lstOfProductObjects.append(objProduct)
        print('Product added to list.')

    # Let user save current data to file and exit program
    elif strChoice.strip() == '3':
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        print('Product list saved to file. Goodbye!')
        break

    else:
        print('Please enter a number from 1 to 3.')

# Main Body of Script END ------------------------------------------------- #

