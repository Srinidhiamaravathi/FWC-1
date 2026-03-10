import numpy as np
import matplotlib.pyplot as plt

print("\nQUESTION 59 – Seven Segment Display Logic\n")

# Inputs
P1 = np.array([0,1,0,1])
P2 = np.array([0,0,1,1])

# Segment logic
g = P1 | P2

print("P1 P2 g")

for i in range(4):
    print(P1[i], P2[i], g[i])

x = np.arange(4)

plt.figure()

plt.step(x, P1, where='post', label="P1")
plt.step(x, P2, where='post', label="P2")
plt.step(x, g, where='post', label="Segment g")

plt.title("Question 59 – Seven Segment Output")
plt.xlabel("Input Combination")
plt.ylabel("Logic Level")

plt.grid()
plt.legend()

plt.savefig("graph.png")
plt.show()
