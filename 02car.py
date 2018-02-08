class car(object):

    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0

    # def tax(self):
    #     if self.price > 10000:
    #         self.tax = self.price*.15
    #     elif self.price <= 10000:
    #         self.tax = self.price*.12
    #   return self

    def display_all(self):
        if self.price > 10000:
            self.tax = float(.15)
        elif self.price <= 10000:
            self.tax = float(.12)
        print "Price: $", self.price, "\nSpeed:", self.speed, "\nFuel:", self.fuel, "\nMileage:", self.mileage, "\nTax:", self.tax
        return self

car1 = car(10000, "100mph", "Full", "50mpg")
car2 = car(5000, "150mph", "Empty", "20mpg")
car3 = car(65000, "200mph", "Full", "15mpg")
car4 = car(2000, "75mph", "Kind of Full", "50mpg")
car5 = car(5500, "100mph", "Empty", "45mpg")
car6 = car(150000, "500mph", "Kind of Full", "45mpg")

car1.display_all()