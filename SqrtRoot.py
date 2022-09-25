import math
# x^2 -2x + 1 = 0
a = 1
b = -2
c = 1

# (x-1)(x-1)
# x^2 -1x -1x +1 
# x^2 -2x +1

def mathsqrt(a,b,c):
  if(b**2-4*a*c < 0):
    print("Input #s are negative discriminant")
    return()
  root1= ((-1*b+math.sqrt(b**2-4*a*c))/(2*a))
  root2 =((-1*b-math.sqrt(b**2-4*a*c))/(2*a))
  return [root1,root2]
# 1*(-1)^2 + 5(-1) + 4
print(mathsqrt(11, 46, 7))
# -1*0 math.sqrt (3**2-4*1*4) / (2*1)
# -1 math.sqrt (4)/2