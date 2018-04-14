#Find the highest common factor between two numbers.
#1. Normal way
x = int(input())
y = int(input())

if x < y :
  small = x
else:
  small = y
  
for i in range(1,small+1):
  if (x%i == 0) and (y%i == 0):
    hcf = i

print("HCF is: ",hcf)

#2. Using Eculidean 
 
'''
Here we loop until y becomes zero. 
The statement x, y = y, x % y does swapping of values in Python. 

In each iteration, we place the value of y in x and the remainder (x % y) in y, simultaneously. 
When y becomes zero, we have H.C.F. in x.
'''


# This function implements the Euclidian algorithm to find H.C.F. of two numbers

while(y):
    x, y = y, x % y

return x
