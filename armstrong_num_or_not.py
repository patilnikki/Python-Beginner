#check if the given number is armstrong or not an armstrong

num = 153  #num = int(input())
sum = 0
temp = num 

power = len(str(num))
while(temp > 0):
  digit = temp % 10
  sum += digit ** power
  temp = temp // 10
  
if(num == sum):
  print("the given number is armsrong")
else:
  print("the given number is not a armstrong number")
  


