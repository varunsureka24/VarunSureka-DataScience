import numpy as np
import os
from numpy import pi

from pyrsistent import v
os.system('clear')

np.zeros((3, 4))
np.ones((2, 3, 4), dtype=np.int16)
np.empty((2, 3))

np.arange(10, 30, 5)
np.arange(0, 2, 0.3)

np.linspace(0, 2, 9)
x = np.linspace(0, 2 * pi, 100)
f = np.sin(x)