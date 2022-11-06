

import matplotlib.pyplot as plt
import numpy as np

import statsmodels.api as sm


connection = open(file='lineVSactual-1 (1).csv',mode='r')
txt = connection.read()
connection.close()

data = txt.split('\n')
line_actual = []

for row in data[1:-1]:
    row_list = row.split(',')
    numbers  = [float(row_list[-2]), float(row_list[-1])]
    line_actual.append(numbers)

arr = np.array(line_actual)
#https://www.statology.org/ols-regression-python/
x = sm.add_constant(arr[:,0])
y = arr[:,1]
model = sm.OLS(y, x).fit()

intercept = model.params[0]
slope = model.params[1]

plt.scatter(x = arr[:,0], y = arr[:,1])
plt.plot([-20,20],[intercept-slope*20,intercept+slope*20])
plt.show()
print(f"Linear equation is actual score = {intercept} + {slope}*line")
print(f"The p value of the intercept is {model.pvalues[0]} which is above 0.05 which means intercept is not significantly different from 0")
print(f"The p value of the slope is {model.pvalues[1]} which is below 0.05 which means slope is significantly different from 0")
print("The betting line in NFL predicts opposite of the actual outcome of the games because the slope is negative")