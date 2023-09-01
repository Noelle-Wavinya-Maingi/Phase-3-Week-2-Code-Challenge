from Review import Review
from Restaurant import Restaurant1, Restaurant2

#Define the customer class and class attribute to store all the customer instances
class Customer:
    all_customers = []

# Define a constructor method to initialize the customer object and initialize the first name and last name then add the instance to the all_customers list.
    def __init__(self, first_name, last_name):
        if type(first_name) != str or type(last_name) != str:
            raise ValueError("Your first and last name should be a string!")
        self._first_name = first_name
        self._last_name = last_name
        self._reviews = [] #a list to store reviews given by a customer
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
    
#Define a method to get the list of restaurants the customer has reviewed and add a review for a restaurant.
    def restaurants(self):
        restaurant_set = set()
        for review in Review.all():
            if review.customer() == self:
                restaurant_set.add(review.restaurant())
        return list(restaurant_set)
    
    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self._reviews.append(review)
        restaurant.add_review(review)

    def num_reviews(self):
        return len(self._reviews)
    
#A class method to find customers by full name
    @classmethod
    def find_by_fullname(cls, fullname):
        for customer in cls.all_customers:
            if customer.full_name() == fullname:
                return customer
        return None

#A class method to find customers by first name
    @classmethod
    def find_by_first_name(cls, firstname):
        matching_name =[]
        for customer in cls.all_customers:
            if customer.get_first_name() == firstname:
                matching_name.append(customer)
        return matching_name

# A class method to return all the customer instances.
    @classmethod
    def all(cls):
        return cls.all_customers


#Test Cases
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")
customer3 = Customer('Mary', 'John')
customer5 = Customer("John", "Doe")


print(customer1.get_first_name())  # Output: John
print(customer1.get_last_name())  #Output: Doe
# print(customer1.full_name())

customer1.add_review(Restaurant1, 3)
customer1.add_review(Restaurant2, 5)
customer2.add_review(Restaurant1, 4.5)

all_customers = Customer.all()
for customer in all_customers:
    print(customer.full_name())

print("Restaurants reviewed by customer1:", [restaurant.name() for restaurant in customer1.restaurants()])
print("Restaurants reviewed by customer2:", [restaurant.name() for restaurant in customer2.restaurants()])

print ("Number of reviews by customer1 is:",customer1.num_reviews(), "reviews.")

find_customer = Customer.find_by_fullname("John Doe")
if find_customer:
    print("Found customer: ", find_customer.full_name())
else:
    print("Customer not found!")

mactching_name = Customer.find_by_first_name("John")
matching_name_list = [customer.full_name() for customer in mactching_name]
print("Matching customer: ", matching_name_list)

try:
    customer4 = Customer("123", "Smith")
except ValueError as e:
    print(e)