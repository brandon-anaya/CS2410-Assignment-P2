#Draw a scatter graph that shows points in even position with red, and points in odd position in green
from matplotlib import lines
import pandas as pd
import matplotlib.pyplot as plt

ex = []
ey = []
ox = []
oy = []
count = 0
i = 1
f = open('file')
for line in f.readlines():
    if count % 2 == 0:
            info = lines.split("    ")
            ex.append(int(info[1]))
            ey.append(int(info[2]))
            count +=1

        
plt.scatter(ex, ey, color='red')
plt.scatter (ox, oy, color = 'green')
plt.title('Scatter Graph of all 5000 points')
plt.xlabel('Even')
plt.ylabel('Odd')
plt.show()