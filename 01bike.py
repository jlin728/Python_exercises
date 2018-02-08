# Assignment: Bike



# Which methods can return self in order to allow chaining methods?

#NOTES ----- "return self" is necessary for chaining, otherwise it breaks.

# declare a class and give it name User
# class User(object):
#     # the __init__ method is called every time a new object is created
#     def __init__(self, name, email):
#         # set some instance variables. just like any variable we can call these anything
#         self.name = name
#         self.email = email
#         self.logged = False
#     # this is a method we created to help a user login
#     def login(self):
#         self.logged = True
#         print self.name + " is logged in."
#         return self
# #now create an instance of the class
# new_user = User("Anna","anna@anna.com")
# print new_user.email
# copy

# Create a new class called Bike with the following properties/attributes:
# price  max_speed  miles

class bike(object):
# Use the __init__() function to specify the price and max_speed of each instance (e.g. bike1 = Bike(200, "25mph"); In the __init__() also write the code so that the initial miles is set to be 0 whenever a new instance is created.
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
#never return in INIT---- hates it

# displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
    def displayInfo(self):
        print "Price: $", self.price, "\nMax speed:", self.max_speed, "\nMiles recorded:", self.miles 
        return self

# ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
    def ride(self):
        self.miles += 10
        #self.miles += 1 to add to 
        print "Riding ... ", self.miles
        return self

# reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...
# Have the first instance ride three times, reverse once and have it displayInfo(). Have the second instance ride twice, reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().

# What would you do to prevent the instance from having negative miles?
    def reverse(self):
        if self.miles >= 5:
            self.miles -= 5
        print "Reversing...", self.miles
        return self


# inheritance 
# class motor(bike):
#    def __init__(self, price, max_speed, miles)
#         super(motor, self).__init__(
#             price, max_speed, miles)
#         self.price = name
#         self.max_speed = max_speed
#         self.miles = 0
#         #never return in INIT---- hates it
#     def displayInfo():
#         return self
        
#     def ride():
#         #self.miles += 1 to add to 
#         return self
#     def reverse(self, parameter_list):
#         return self

# Create 3 instances of the Bike class.
bike1 = bike(95, "60mph")
bike2 = bike(1000, "180mph")
bike3 = bike(400, "80mph")

#1
#bike1.ride().ride().ride().reverse().displayInfo()
#2
#bike2.ride().ride().reverse().reverse().displayInfo()
#3
bike3.reverse().reverse()

#print bike1.ride().reverse() #chaining