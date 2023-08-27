#Define the customer class and class attribute to store all the customer instances
class Customer:
    all_customers = []

# Define a constructor method to initialize the customer object and initialize the first name and lass name then add the instance to the all_customers list.
    def __init__(self, first_name, last_name):
        if type(first_name) != str or type(last_name) != str:
            raise ValueError("Your first and last name should be a string!")
        self._first_name = first_name
        self._last_name = last_name
        Customer.all_customers.append(self)

# Define a method to retrieve the first name of the customer
    def get_first_name(self):
        return self._first_name
    
# Define a method to retrieve the last name of the customer
    def get_last_name(self):
        return self._last_name

# Define methods to set new first name and last name
    def set_first_name(self, new_first_name):
        if type(new_first_name) != str:
            raise ValueError("Your first name should be a string!")
        self._first_name = new_first_name

    def set_last_name(self, new_last_name):
        if type(new_last_name) != str:
            raise ValueError("Your last name should be a string!")
        self._last_name = new_last_name
    
# Define a method to retrieve the full name of the customer    
    def full_name(self):
        return f"{self._first_name} {self._last_name}"
    
# A class method to return all the customer instances.
    @classmethod
    def all(cls):
        return cls.all_customers

customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")
customer3 = Customer('Mary', 'John')


print(customer1.get_first_name())  # Output: John
print(customer1.get_last_name())  #Output: Doe
# print(customer1.full_name())

customer1.set_first_name("Alice")
customer1.set_last_name("Johnson")
# print(customer1.full_name())

all_customers = Customer.all()
for customer in all_customers:
    print(customer.full_name())

try:
    customer4 = Customer("123", "Smith")
except ValueError as e:
    print(e)

