from numpy import positive
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('5000_points.txt',sep='\s+',header=None)
data = pd.DataFrame(data)
x_even 
y_even

x_odd
y_odd

x = data[0,2,4]
y = data[1]

plt.scatter(x_even,y_even,color='red')
plt.scatter(x_odd,y_odd,color='green')

less_than = []
equal = []
greater_than = []

for value in data:
    if value[0] > value[1]:
        greater_than += 1
    elif value[0] < value[1]:
        less_than += 1
    else:
        equal += 1
