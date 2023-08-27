from Review import Review

class Restaurant:
#Initialize the restaurant object with a name and check if the name is a string, if not it should raise ValueError
    def __init__(self, name):
        if type(name) != str:
            raise ValueError("The name of the restaurant should be a string!")
        self._name = name
    #Initialize an empty list to store the reviews.
        self._reviews = []
    
#Returns the name of the restaurant
    def name(self):
        return self._name
    
#Method to add a review to the list of reviews for the restaurant
    def add_review(self, review):
        self._reviews.append(review)

#Method to return a ;ist of reviews
    def reviews(self):
        return self._reviews
    
#A method to return the list of customers who have reviewed the restaurants.
    def customers(self):
        customer_set = set()
        for review in self._reviews:
            customer_set.add(review.customer())
        return list(customer_set)
    
#A method to calculate and return the average star rating for the restaurants reviews    
    def average_star_rating(self):
        total_rating = sum([review.rating()for review in self._reviews])
        num_rating = len(self._reviews)

        if num_rating == 0:
            return 0
        else:
            return total_rating / num_rating

#Restaurant instances  
Restaurant1 = Restaurant("Cafe Deli")
Restaurant2 = Restaurant("The Bistro")

#Review instances
review1 = Review("John Doe", Restaurant1, 4)
review2 = Review("Jane Smith", Restaurant2, 4.5)
review3 = Review("John Doe", Restaurant2, 5)

#Add reviews to the respective restaurants
Restaurant1.add_review(review1)
Restaurant2.add_review(review2)
Restaurant2.add_review(review3)

#Prints restaurant names
print(Restaurant1.name())
print(Restaurant2.name())

#Print ratings for the reviews of each restaurant
print("Reviews for Restaurant1:", [review.rating() for review in Restaurant1.reviews()])
print("Reviews for Restaurant2:", [review.rating() for review in Restaurant2.reviews()])

#Print customers who reviewed each restaurant
print("Customers who reviewed Restaurant1:", Restaurant1.customers())
print("Customers who reviewed Restaurant2:", Restaurant2.customers())

print(f"Average star rating for {Restaurant1.name()}: {Restaurant1.average_star_rating()}")
print(f"Average star rating for {Restaurant2.name()}: {Restaurant2.average_star_rating()}")
