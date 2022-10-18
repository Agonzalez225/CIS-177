F = [1,1]

for num in list(range(20)):
  F.append(F[-2] + F[-1])
print(F)

def Converging_Ratios(F):
  ratios = []
  for i in range(1,20):
    print(F[i]/F[i-1]) 
    ratios.append(F[i]/F[i-1])
  return ratios
Ratios = Converging_Ratios(F)
print(Ratios)
GoldenRatio = 1.618033989
errors = []
for i in range(0,19):
  Ratios[i] -GoldenRatio
  errors.append(abs(Ratios[i] -GoldenRatio))
print(errors)
import math
import numpy as np

# q = np.log(e[N+1]/e{N]) / np.log(e[N]/e[N-1])
Qs = []
for N in range(1,18):
  q = np.log(errors[N+1]/errors[N]) / np.log(errors[N]/errors[N-1])
  Qs.append(np.log(errors[N+1]/errors[N]) / np.log(errors[N]/errors[N-1]))
print(Qs[-5:])

