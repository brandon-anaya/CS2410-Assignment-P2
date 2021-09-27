#Draw a scatter graph to show all points.
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('5000_points.txt',sep='\s+',header=None)
data = pd.DataFrame(data)

import matplotlib.pyplot as plt
x = data[0]
y = data[1]

plt.scatter(x,y,color='green')
plt.title('Scatter Graph of all 5000 points')
plt.show()