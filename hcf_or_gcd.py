#Find the highest common factor between two numbers.

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

