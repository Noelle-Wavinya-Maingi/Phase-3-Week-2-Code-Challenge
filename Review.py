class Review:
    # Class attribute to store all review instances
    all_reviews = []

    # Initialize a review object with a customer, restaurant, and rating
    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review.all_reviews.append(self)  # Add the review instance to the all_reviews list

    # Return the rating of the review
    def rating(self):
        return self._rating
    
    # A class method to return all the review instances
    @classmethod
    def all(cls):
        return cls.all_reviews
