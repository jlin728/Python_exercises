class thing(object):

    def __init__(self, name, price, weight, brand, status):
        self.name = name
        self.price = price
        self.weight = weight
        self.brand = brand
        self.status = status

    def sell(self):
        # if self.status == "For:
        #     print "For Sale"
        self.status = "SOLD"
        # else:
            # print "SOLD"
        return self

    def tax(self, tax):
        # print "Tax:", 
        self.price = (self.price * tax)+self.price
        return self
    
    def returns(self, reason):
        # self.reason = reason
        if reason == "Defective":
            self.status = "Defective"
            self.price = 0
            # print "Updated Status: ", self.status, self.price
        elif reason == "New":
            self.status = "For Sale"
            # print "Updated Status: ", self.status, self.price
        elif reason == "Used":
            self.status = "Used"
            self.price = self.price-(self.price*.20)
            
            # print "Updated Status: ", self.status, self.price
        return self

    def display_all(self):
        print "Name: ", self.name, "\nPrice: $", self.price, "\nWeight:", self.weight, "\nBrand:", self.brand, "\nStatus:", self.status
        return self

thing1 = thing("Thing You Need", 52, "1 oz.", "By Woots", "For sale")

#thing1.tax(.25)
thing1.sell().tax(.25).returns("New").display_all()
