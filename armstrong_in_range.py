#find all the armstrong numbers in given range range

lower = 100 #lower = int(input())
upper = 500 #upper = int(input())

for i in range(lower,upper):
  power = len(str(i))
  
  sum = 0 
  temp = i
  
  while(temp > 0):
    digit = temp % 10  #3
    sum += digit ** power
    temp = temp // 10
  if i == sum:
    print(i)
