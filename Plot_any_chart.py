#Plot a chart of your choice using any data given in the data file
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('planets.csv')
Planets = list(df.iloc[:, 0])
Diameter = list(df.iloc[:, 2])

plt.bar(Planets,Diameter,color='green')
plt.ylabel("Planets")
plt.title("Diameter of Planets")
plt.show()