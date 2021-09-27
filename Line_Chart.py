#Draw a (multiple) line chart with x-axis as planets and y-axis as the gravity
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('planets.csv')
X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 4])

plt.plot(X, Y, color='green', marker='o', linestyle='solid')

plt.title("Planets vs. Gravity")

plt.xlabel("Planets")
plt.ylabel("Gravity")
plt.show()
