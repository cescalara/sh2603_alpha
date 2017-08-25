import numpy as np
from matplotlib import pyplot as plt

# Measured pressure and energies from the lab
P = [0.02, 0.1, 0.21, 0.3, 0.35, 0.4, 0.45, 0.5, 0.6]
E_cm = [5804, 5462, 4950, 4492, 4265, 3943, 3719, 3360, 2678]
E_am = [5485, 5140, 4599, 4119, 3874, 3541, 3229, 2892, 2145]
E_pu = [5156, 4792, 4218, 3709, 3439, 3073, 2769, 2389, 0]

# Plot to check
plt.plot(P, E_cm, P, E_am, P, E_pu)
plt.show()

# Function to describe relationship between x and P
def P_to_x(P, P_0, x_0):
    x = (P_0 * x_0) / P
    return x

# Values for which 0 energy is observed
P_0 = 0.8 # [bar]
x_0 = 5.4 # [cm]

x = []
for i in range(len(P)):
    x.append(P_to_x(P[i], P_0, x_0))
x = np.array(x)


