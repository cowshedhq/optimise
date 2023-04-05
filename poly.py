import numpy as np
import matplotlib.pyplot as plt

def poly(x):
    return (x+1)*x*(x-1)*(x-4)

x = np.linspace(-2,4.5,100)
y = poly(x)
plt.ion()
plt.plot(x,y)

plt.show()
