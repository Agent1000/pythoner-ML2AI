import numpy as Np
import matplotlib.pyplot as plt
x=Np.linspace(-5,5,100)
y=2*x+1

plt.plot(x,y,'r',label='y=2*x+1')
plt.xlabel('x')
plt.xlabel('y')
plt.legend(loc="upper left")
plt.title("graph y=2*x+1")
plt.grid()
plt.show()