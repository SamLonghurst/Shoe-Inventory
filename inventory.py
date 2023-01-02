from itertools import islice
#========The beginning of the class==========
class Shoe(object):

    def __init__(self,country,code,product,cost,quantity):
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        print(self.cost)

    def get_quantity(self):
        '''
        Add the code to return the quantity of the shoes.
        '''
        print(self.quantity)
    def __str__(self):
        '''
        Add a code to returns a string representation of a class.
        '''
        print(f"{self.product},{self.code},{self.cost},{self.quantity}")


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    # Read file and store in variable with error handling
    try:

        inv_file = open('inventory.txt','r')

    except FileNotFoundError:
        
        print("This file does not exist in this path")

    # Split each line into the attributes of the shoe object, ignoring the first line
    for each_shoe in islice(inv_file, 1, None):

        each_shoe_element = each_shoe.split(",")
        shoe_country = each_shoe_element[0]
        shoe_code = each_shoe_element[1]
        shoe_product = each_shoe_element[2]
        shoe_cost = float(each_shoe_element[3])
        shoe_quantity = float(each_shoe_element[4])

        # Append each line to the shoe list
        shoe_list.append(Shoe(shoe_country,shoe_code,shoe_product,shoe_cost,shoe_quantity))

    #inv_file.close()   

def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    # Assign each attribute/variable with user input
    shoe_country = input("Enter a Country: ")
    shoe_code = input("Enter the Code: ")
    shoe_product = input("Enter the name of the Product")
    shoe_cost = float(input("Enter the Cost: "))
    shoe_quantity = float(input("Enter the Quantity"))
    
    # Add the entries to a shoe object then append to the shoe list
    shoe_list.append(Shoe(shoe_country,shoe_code,shoe_product,shoe_cost,shoe_quantity))

def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    # Print each shoe in the format set by the __str__ function
    for each_shoe in shoe_list:

        each_shoe.__str__()
    
def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    # Check the quantity value for each shoe and return the minimum value
    min_q_shoe = min(each_shoe.quantity for each_shoe in shoe_list)

    # Find the shoe that has the quantity value matching the min_q_shoe value
    for each_shoe in shoe_list:

        if each_shoe.quantity == min_q_shoe:

            print(f"The Shoe with the least amount of stock is: {each_shoe.country}, {each_shoe.code}, {each_shoe.product}, {each_shoe.cost}, {each_shoe.quantity}")

            # Ask user to input an amount to increase the quantity by and add it to the current quantity value
            add_stock = int(input("Enter the quantity you would like to add"))

            each_shoe.quantity += add_stock

            # Print shoe with updated quantity value
            print(f"This Shoes quantity has been updated: {each_shoe.country}, {each_shoe.code}, {each_shoe.product}, {each_shoe.cost}, {each_shoe.quantity}")

    # Clear file and write the heading categories
    inv_file = open ('inventory.txt','w')

    inv_file.write("Country,Code,Product,Cost,Quantity\n")

    # Append the update shoes to the inventory file
    with open ('inventory.txt','a'):

        for each_shoe in shoe_list:

            inv_file.write(f"{each_shoe.country},{each_shoe.code},{each_shoe.product},{each_shoe.cost},{each_shoe.quantity}\n")

def seach_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

    # User entry for shoe code
    user_entry_shoe_code = input("Please enter a shoe code: ")

    # Check all shoes and return shoe with match shoe code
    for each_shoe in shoe_list:

        if each_shoe.code == user_entry_shoe_code:

            print(f"{each_shoe.country}, {each_shoe.code}, {each_shoe.product}, {each_shoe.cost}, {each_shoe.quantity}")

def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    # Print each shoe in the shoe list with total value being the cost * quantity
    for each_shoe in shoe_list:

        print(f"Total value is : £{each_shoe.quantity * each_shoe.cost} for {each_shoe.country}, {each_shoe.code}, {each_shoe.product}, £{each_shoe.cost}, {each_shoe.quantity}")

def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    # Check the quantity value for each shoe and return the minimum value
    max_q_shoe = max(each_shoe.quantity for each_shoe in shoe_list)

    # Find the shoe that has the quantity value matching the min_q_shoe value
    for each_shoe in shoe_list:

        if each_shoe.quantity == max_q_shoe:

            # Display this shoe as on Sale
             print(f'''The Shoe with the Most amount of stock is: {each_shoe.country}, {each_shoe.code}, {each_shoe.product}, {each_shoe.cost}, {each_shoe.quantity}
             - This item is on sale''')


# This function must be used first in order for the functions to work 
read_shoes_data()

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
while True:

    main_menu = input('''Choose from the menu
    r = read shoes data
    c = capture shoes
    va = view all shoes
    rs = re-stock
    s = search for a shoe
    vpi = value per item
    hq = highest quantity item
    e = exit
    : ''').lower()

    if main_menu == "r":

        read_shoes_data()

    elif main_menu == "c":

        capture_shoes()

    elif main_menu == "va":

        view_all()
    
    elif main_menu == "rs":

        re_stock()

    elif main_menu == "s":

        seach_shoe()

    elif main_menu == "vpi":

        value_per_item()

    elif main_menu == "hq":

        highest_qty()

    elif main_menu == "e":

        exit()

    else:

        print("This is not an option")