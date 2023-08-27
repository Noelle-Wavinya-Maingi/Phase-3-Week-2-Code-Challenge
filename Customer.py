#Define the customer class and class attribute to store all the customer instances
class Customer:
    all_customers = []

# Define a constructor method to initialize the customer object and initialize the first name and lass name then add the instance to the all_customers list.
    def __init__(self, first_name, last_name):
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
        self._first_name = new_first_name

    def set_last_name(self, new_last_name):
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

print(customer1.get_first_name())  # Output: John
print(customer1.get_last_name())
print(customer1.full_name())

