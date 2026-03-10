import numpy as np
import matplotlib.pyplot as plt

kmap = np.array([
    [0,1,0,0],
    [0,1,1,1],
    [1,1,1,0],
    [0,0,1,0]
])

print("K-map Matrix:")
print(kmap)

plt.figure()
plt.imshow(kmap)

for i in range(4):
    for j in range(4):
        plt.text(j, i, kmap[i][j], ha='center', va='center')

plt.title("Q8 Karnaugh Map")
plt.xlabel("PQ (00 01 11 10)")
plt.ylabel("RS (00 01 11 10)")
plt.colorbar()

plt.savefig("graph.png")
plt.show()
