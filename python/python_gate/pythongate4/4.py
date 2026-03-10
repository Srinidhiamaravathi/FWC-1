import numpy as np
import matplotlib.pyplot as plt

print("\nQUESTION 41 – Circuit Output\n")

# Inputs
A = np.array([0,0,1,1])
B = np.array([0,1,0,1])

# Logic function
Q = (~A & 1) | B   # A' + B

print("A B Q")

for i in range(4):
    print(A[i], B[i], Q[i])

x = np.arange(4)

plt.figure()

plt.step(x, A, where='post', label="A")
plt.step(x, B, where='post', label="B")
plt.step(x, Q, where='post', label="Q")

plt.title("Question 41 Circuit Output")
plt.xlabel("Input Combination")
plt.ylabel("Logic Level")

plt.grid()
plt.legend()

plt.savefig("graph.png")
plt.show()
