# coding: utf-8
import pandas as pd
df = pd.read_csv("large_files/train.csv")
df.shape
M = df.as_matrix()
im = M[0, 1:]
im.shape
im = im.reshape(28, 28)
im.shape
import matplotlib.pyplot as plt
plt.imshow(im)
plt.show()
M[0,0]
plt.show()
plt.imshow(im, cmap='gray')
plt.show()
plt.imshow(255 - im, cmap='gray')
plt.show()
