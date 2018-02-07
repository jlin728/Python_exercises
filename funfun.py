#Odd Even

def oddEven(start, end):
    for i in range (start, end+1):
        if i % 2 == 0:
            print "Number is",i,". This is an even number."
        else: #i % 2 == 1:
            print "Number is",i,". This is an odd number."

#test case oddEven(2,15)

#Multiply
#     for i in multiply:
#a=[1,2,3,4]
def multiply(list, mult):
    b = []
    for i in range(0,len(list)):
        b.append(list[i]*mult) 
    print b
#testcase- multiply([1,2,3], 5)




# Hacker Challenge:
# Write a function that takes the multiply function call as an argument. Your new function should return the multiplied list as a two-dimensional list. Each internal list should contain the 1's times the number in the original list. Here's an example:

# def layered_multiples(arr):
#   # your code here
#   return new_array
# x = layered_multiples(multiply([2,4,5],3))
# print x
# # output
# >>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
def mult2(list, num):
    x = []
    for i in range(len(list)):
        list2 = [list[i]*num*"1"]
        x.append(list2)
    print x

mult2([2,3,8], 2)

