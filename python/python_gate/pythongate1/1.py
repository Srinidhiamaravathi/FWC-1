import numpy as np
import matplotlib.pyplot as plt

# Input combinations
A = np.array([0, 0, 1, 1])
B = np.array([0, 1, 0, 1])

# Logic gate outputs
NAND = 1 - (A & B)
NOR = 1 - (A | B)

# Print truth table
print("Truth Table")
print("A B NAND NOR")

for i in range(4):
    print(A[i], B[i], NAND[i], NOR[i])

# X-axis positions
x = np.arange(4)

# Plot the waveforms
plt.step(x, A, where='post', label='A')
plt.step(x, B, where='post', label='B')
plt.step(x, NAND, where='post', label='NAND')
plt.step(x, NOR, where='post', label='NOR')

# Labels and title
plt.xlabel("Input Combination Index")
plt.ylabel("Logic Level")
plt.title("Universal Gates (NAND and NOR)")

plt.ylim(-0.2, 1.2)
plt.grid()
plt.legend()

plt.show()
