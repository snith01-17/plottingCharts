import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("star_gravity.csv")

df.head()

mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
distance = df["Distance"].to_list()
gravity = df["Gravity"].to_list()

mass.sort()
radius.sort()
gravity.sort()

plt.title("Mass and Radius")
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.plot(radius,mass)
plt.show()

plt.title("Mass vs Gravity")
plt.xlabel("Mass")
plt.ylabel("Gravity")
plt.scatter(gravity,mass)
plt.show()
