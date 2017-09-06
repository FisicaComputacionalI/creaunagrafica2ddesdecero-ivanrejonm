import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0.,5.,0.01)
plt.plot(t,t**2,'y--')
plt.axis([0,5,0,25])
plt.show()
