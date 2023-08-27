class Review:
    # Class attribute to store all review instances
    all_reviews = []

    # Initialize a review object with a customer, restaurant, and rating
    def __init__(self, customer, restaurant, rating):
        if type(rating) != int and type(rating) != float:
            raise ValueError("Rating should be a number")
        
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review.all_reviews.append(self)  # Add the review instance to the all_reviews list

    # Return the rating of the review, the customer and the restaurant
    def rating(self):
        return self._rating
    
    def customer(self):
        return self._customer
    
    def restaurant(self):
        return self._restaurant
    
    # A class method to return all the review instances
    @classmethod
    def all(cls):
        return cls.all_reviews
