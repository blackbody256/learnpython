### TODO:
#   - code a Pants class with the following attributes
#   - color (string) eg 'red', 'yellow', 'orange'
#   - waist_size (integer) eg 8, 9, 10, 32, 33, 34
#   - length (integer) eg 27, 28, 29, 30, 31
#   - price (float) eg 9.28
class Pants:
    def __init__(self,color,waist_size,length,price):
        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price
    
    def change_price (self,new_price):
        self.price = new_price
        
    def discount (self,discount_value):
        return (1-discount_value)*self.price
    

### TODO: Declare the Pants Class 

### TODO: write an __init__ function to initialize the attributes

### TODO: write a change_price method:
#    Args:
#        new_price (float): the new price of the shirt
#    Returns:
#        None

### TODO: write a discount method:
#    Args:
#        discount (float): a decimal value for the discount. 
#            For example 0.05 for a 5% discount.
#
#    Returns:
#        float: the discounted price

def check_results():
    pants = Pants('red', 35, 36, 15.12)
    assert pants.color == 'red'
    assert pants.waist_size == 35
    assert pants.length == 36
    assert pants.price == 15.12
    
    pants.change_price(10) == 10
    assert pants.price == 10 
    
    assert pants.discount(.1) == 9
    
    print('You made it to the end of the check. Nice job!')

check_results()

### TODO:
#   Code a SalesPerson class with the following attributes
#   - first_name (string), the first name of the salesperson
#   - last_name (string), the last name of the salesperson
#   - employee_id (int), the employee ID number like 5681923
#   - salary (float), the monthly salary of the employee
#   - pants_sold (list of Pants objects), 
#            pants that the salesperson has sold 
#   - total_sales (float), sum of sales of pants sold
class SalesPerson:
    def __init__(self,first_name,last_name,employee_id,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.pants_sold = []
        self.total_sales = 0

### TODO: Declare the SalesPerson Class 

### TODO: write an __init__ function to initialize the attributes
###    Input Args for the __init__ function:
#        first_name (str)
#        last_name (str)
#        employee_id (int)
# .      salary (float)
#
# You can initialize pants_sold as an empty list
# You can initialize total_sales to zero.
#
###

    def sell_pants(self,Pants_object):
        self.pants_sold.append(Pants_object)
### TODO: write a sell_pants method:
#
#    This method receives a Pants object and appends
#    the object to the pants_sold attribute list
#
#    Args:
#        pants (Pants object): a pants object
#    Returns:
#        None
    def display_sales(self):
        for pant in self.pants_sold:
            print(f"color: {pant.color}, waist_size: {pant.waist_size}, length: {pant.length}, price: {pant.price}")
### TODO: write a display_sales method:
#    
#    This method has no input or outputs. When this method 
#    is called, the code iterates through the pants_sold list
#    and prints out the characteristics of each pair of pants
#    line by line. The print out should look something like this
#
#   color: blue, waist_size: 34, length: 34, price: 10
#   color: red, waist_size: 36, length: 30, price: 14.15
#
#
#
###
    def calculate_sales(self):
        total_sales = 0
        for pant in self.pants_sold:
            total_sales+=pant.price
        return total_sales
### TODO: write a calculate_sales method:
#      This method calculates the total sales for the sales person.
#      The method should iterate through the pants_sold attribute list
#      and sum the prices of the pants sold. The sum should be stored
#      in the total_sales attribute and then return the total.
#      
#      Args:
#        None
#      Returns:
#        float: total sales
#
###  

    def calculate_commission (self,percentage):
        total_sales = self.calculate_sales()
        total_commission= percentage*total_sales
        return total_commission
        
### TODO: write a calculate_commission method:
#
#   The salesperson receives a commission based on the total
#   sales of pants. The method receives a percentage, and then
#   calculate the total sales of pants based on the price,
#   and then returns the commission as (percentage * total sales)
#
#    Args:
#        percentage (float): comission percentage as a decimal
#
#    Returns:
#        float: total commission
#
#
###

def check_results():
    pants_one = Pants('red', 35, 36, 15.12)
    pants_two = Pants('blue', 40, 38, 24.12)
    pants_three = Pants('tan', 28, 30, 8.12)
    
    salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)
    
    assert salesperson.first_name == 'Amy'
    assert salesperson.last_name == 'Gonzalez'
    assert salesperson.employee_id == 2581923
    assert salesperson.salary == 40000
    assert salesperson.pants_sold == []
    assert salesperson.total_sales == 0
    
    salesperson.sell_pants(pants_one)
    salesperson.pants_sold[0] == pants_one.color
    
    salesperson.sell_pants(pants_two)
    salesperson.sell_pants(pants_three)
    
    assert len(salesperson.pants_sold) == 3
    assert round(salesperson.calculate_sales(),2) == 47.36
    assert round(salesperson.calculate_commission(.1),2) == 4.74
    
    print('Great job, you made it to the end of the code checks!')
    
check_results()

pants_one = Pants('red', 35, 36, 15.12)
pants_two = Pants('blue', 40, 38, 24.12)
pants_three = Pants('tan', 28, 30, 8.12)

salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)

salesperson.sell_pants(pants_one)    
salesperson.sell_pants(pants_two)
salesperson.sell_pants(pants_three)

salesperson.display_sales()



#The answer code
class Pants:
    """The Pants class represents an article of clothing sold in a store
    """
    
    def __init__(self, color, waist_size, length, price):
        """Method for initializing a Pants object
    
        Args: 
            color (str)
            waist_size (int)
            length (int)
            price (float)
            
        Attributes:
            color (str): color of a pants object
            waist_size (str): waist size of a pants object
            length (str): length of a pants object
            price (float): price of a pants object
        """
            
        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price
    
    def change_price(self, new_price):
        """The change_price method changes the price attribute of a pants object
    
        Args: 
            new_price (float): the new price of the pants object
            
        Returns: None
        
        """
        self.price = new_price
    
    def discount(self, percentage):
        """The discount method outputs a discounted price of a pants object

        Args:
            percentage (float): a decimal representing the amount to discount

        Returns:
            float: the discounted price
        """
        return self.price * (1 - percentage)


class SalesPerson:
    """The SalesPerson class represents an employee in the store

    """

    def __init__(self, first_name, last_name, employee_id, salary):
        """Method for initializing a SalesPerson object
        
        Args: 
            first_name (str)
            last_name (str)
            employee_id (int)
            salary (float)

        Attributes:
            first_name (str): first name of the employee
            last_name (str): last name of the employee
            employee_id (int): identification number of the employee
            salary (float): yearly salary of the employee
            pants_sold (list): a list of pants objects sold by the employee
            total_sales (float): sum of all sales made by the employee

        """
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.pants_sold = []
        self.total_sales = 0

    def sell_pants(self, pants_object):
        """The sell_pants method appends a pants object to the pants_sold attribute

        Args: 
            pants_object (obj): a pants object that was sold

        Returns: None

        """

        self.pants_sold.append(pants_object)

    def display_sales(self):
        """The display_sales method prints out all pants that have been sold

        Args: None

        Returns: None

        """

        for pants in self.pants_sold:
            print('color: {}, waist_size: {}, length: {}, price: {}'\
                  .format(pants.color, pants.waist_size, pants.length, pants.price))
    
    def calculate_sales(self):
        """The calculate_sales method sums the total price of all pants sold

        Args: None

        Returns:
            float: sum of the price for all pants sold
        
        """

        total = 0
        for pants in self.pants_sold:
            total += pants.price
            
        self.total_sales = total
        
        return total
    
    def calculate_commission(self, percentage):
        """The calculate_commission method outputs the commission based on sales

        Args:
            percentage (float): the commission percentage as a decimal

        Returns:
            float: the commission due
        """

        sales_total = self.calculate_sales()
        return sales_total * percentage 