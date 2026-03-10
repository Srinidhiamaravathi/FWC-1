import numpy as np
import matplotlib.pyplot as plt

print("\nQUESTION 36 – Boolean Simplification\n")

Y = np.array([0,0,1,1])
Z = np.array([0,1,0,1])

F = 1 - (Y & Z)

print("Y Z F")
for i in range(4):
    print(Y[i], Z[i], F[i])

x = np.arange(4)

plt.figure()
plt.step(x, Y, where='post', label="Y")
plt.step(x, Z, where='post', label="Z")
plt.step(x, F, where='post', label="F = NAND")

plt.title("Q36 NAND Output")
plt.xlabel("Input Combination")
plt.ylabel("Logic Level")

plt.grid()
plt.legend()

plt.savefig("graph.png")
plt.show()
