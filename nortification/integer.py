from matplotlib import pyplot as plt
import numpy as np

def greatest_integer(x):
    return np.ceil(x)
# Generating the data
x = np.linspace(-10, 20, 1000)
y = greatest_integer(x)

 # creating greatest integer graph
fig, ax = plt.subplots()
ax.plot(x,y)

 # Now adding the labels and titles
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Greatest Integer Graph')

plt.show()