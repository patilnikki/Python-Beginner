#Swapping the numbers

x = 10
y = 20

#1. Directly
x,y = y,x
print("x = ",x)
print("y = ",y)

#2. Using temp Varable
temp = x
x = y
y = temp
print("x = ",x)
print("y = ",y)


#3. Using add and subtract operator
x = x+y
y = x-y
x = x-y
print("x = ",x)
print("y = ",y)


#4. Using Multiplication and Division operator
x = x*y
y = x/y
x = x/y
print("x = ",x)
print("y = ",y)


#5. Using XOR operator
x = x^y
y = x^y
x = x^y
print("x = ",x)
print("y = ",y)
