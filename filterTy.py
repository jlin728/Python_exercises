sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']
uN = 1+2j #test case for my else statement of Unknown class/type
# set X variable to above variable you want to test, otherwise you will have to change all instances of that var name within the if / else statement
x = uN

if isinstance(x , int) and x < 100:
    print "That's a small number"
elif isinstance(x , int) and x >= 100:
    print "THAT'S A BIG NUMBER"
elif isinstance(x, str) and len(x) < 50:
    print "Short sentence"
elif isinstance(x, str) and len(x) >= 50:
    print "LONG SENTENCE!"
elif isinstance(x, list) and len(x) < 50:
    print "short list"
elif isinstance(x, list) and len(x) >= 50:
    print "BIG LIST!"
else:
    print ("Unknown")

''' print (isinstance (spL, int))

'if isinstance(mS, int):
    
if type() === int <= 100:
    print "That's a big number!"
else:
    print "That's a small number..".


if type() == int <= 100:
    print "That's a big number!"
elif condition:
    do something else
else:
    do this instead
'''
