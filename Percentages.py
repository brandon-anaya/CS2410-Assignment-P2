#Draw a pie chart showing the percentage of planets with negative rotation values vs. positive rotation values.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('planets.csv')
rotalist = list(df.iloc[:, 6])
labels = ['Negative Rotation', 'Positive Rotation']
sizes = [15,85]
neg = 0
pos = 0
for value in rotalist:
    if value < 0:
        neg+=1
    else: 
        pos += 1
rotalist =[neg,pos]

plt.pie(rotalist, labels = labels,autopct='%1.1f%%’',shadow=True, startangle=90)
plt.axis('equal')
plt.show()



