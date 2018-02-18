class card(object):

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def shuffle(self):
        if self.price > 10000:
            self.tax = float(.15)
        elif self.price <= 10000:
            self.tax = float(.12)
        print "Price: $", self.price, "\nSpeed:", self.speed, "\nFuel:", self.fuel, "\nMileage:", self.mileage, "\nTax:", self.tax
        return self

    def deal(self):

        return self

card1.display_all()
