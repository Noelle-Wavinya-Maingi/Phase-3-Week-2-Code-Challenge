class Restaurant:
#Initialize the restaurant object with a name and check if the name is a string, if not it should raise ValueError
    def __init__(self, name):
        if type(name) != str:
            raise ValueError("The name of the restaurant should be a string!")
        self._name = name
    
#Returns the name of the restaurant
    def name(self):
        return self._name
    
Restaurant1 = Restaurant("Cafe Deli")
Restaurant2 = Restaurant("The Bistro")

print(Restaurant1.name())
print(Restaurant2.name())