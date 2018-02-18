from random import shuffle
class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

class Deck(object):
    def __init__(self):
        self.list1 = []
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        values = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        for idx in range(len(suits)):
            for i in range(len(values)):
                self.list1.append(Card(suits[idx], values[i]))

    def shuffle1(self):
        print shuffle(self.list1)
        return self

    def dealCard(self):
        print self.list1[len(self.list1)-1]
        self.list1.pop()
    
    def display(self):
        print self.list1
        print len(self.list1)

    
deck1 = Deck()
deck1.shuffle1()
deck1.dealCard()
deck1.display()
