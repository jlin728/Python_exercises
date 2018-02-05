'''
# Find Replace

words = "It's Thanksgiving day. It's my birthday, too!"
print words.find("day")
print words.replace("day", "month", 1) # last  parameter states the first occurence


# Min Max

x = [64,-45,95,2,3,5,1,3514,-2,5212,212,-55212,545212,52,-78,6,333,41,4]
print max(x)
print min(x)

# First Last

x = ["Jihfan", 2,6,9,87,"Lin"]
print x[0]
print x[-1]
newList = [x[0], x[-1]]
print  newList

'''

#New List

#sort
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x #without print x will return NONE

#or print sorted(x)

#Split list in half

y = x[:len(x)/2]
z = x[len(x)/2:]

z.insert(0, y)
print z



