def stepCounter(n):
  i = 0
  while n!=1:
    if n %2 == 1:
      n = 3*n+1
     
    else :
      n = n/2
    i = i + 1
  
   # print(n)

   # print("The number of steps is : " +str(i))

  return i


for num in list(range(5, 21)):
  print("for n = "+str(num)+", the number of steps is : "+str(stepCounter(num)))