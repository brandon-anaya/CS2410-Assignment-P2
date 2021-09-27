#Draw a bar chart showing the density of the planets
# # Import the modules
from numpy import negative, positive
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('planets.csv')
  
df = pd.DataFrame(data)
  
X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 3])
  
# Plot the data using bar() method
plt.bar(X, Y, color='blue')
plt.title("Density of Planets")
plt.xlabel("Planets")
plt.ylabel("Density")
  
# Show the plot
plt.show()