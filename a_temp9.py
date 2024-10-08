import numpy as np
import matplotlib.pyplot as plt

w = 10
h = 10
fig = plt.figure(figsize=(8, 8))
columns = 4
rows = 5
img = np.random.randint(10, size=(h,w))
fig.add_subplot(rows, columns, 1)
plt.imshow(img)
plt.show()