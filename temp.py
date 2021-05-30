import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-4,5,1)
plt.title("curve chart")

y=x**3-x*x+10*x+5

plt.plot(x,y)
plt.axhline(y=0)
plt.axvline(x=0)
plt.show()

x = np.linspace(-5,5,100)
plt.title("curve chart")

y = x*x
plt.plot(x,y)
y = x*x+5
plt.plot(x,y)
y = -x*x
plt.plot(x,y)
y = (x-3)**2
plt.plot(x,y)

A, =plt.plot(x,y)
B, =plt.plot(x,y)
C, =plt.plot(x,y)
D, =plt.plot(x,y)
plt.legend([A,B,C,D],["x*x","x*x+5","-x*x","(x-3)**2"])

plt.show()
