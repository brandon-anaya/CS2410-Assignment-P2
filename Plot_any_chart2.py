import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('5000_points.txt',sep='\s+',header=None)
data = pd.DataFrame(data)

with open('5000_points.txt') as f:
    lines = f.readlines()
    x = [line.split()[0] for line in lines]
    y = [line.split()[1] for line in lines]

x = data[0]
y = data[1]

plt.scatter(x,y,color='green')
plt.show()