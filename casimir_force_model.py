import numpy as np
import matplotlib.pyplot as plt

# Constants
hbar = 1.0545718e-34
c = 3e8
pi = np.pi

def casimir_force(d, epsilon_r=1):
    return -(pi**2 * hbar * c) / (240 * d**4) * (1 / epsilon_r)

# Distances (meters)
d_vals = np.linspace(1e-9, 1e-7, 100)
normal_force = casimir_force(d_vals)
meta_force = casimir_force(d_vals, epsilon_r=3.5)

plt.plot(d_vals * 1e9, normal_force * 1e5, label='Vacuum')
plt.plot(d_vals * 1e9, meta_force * 1e5, label='Metamaterial (εr=3.5)', linestyle='--')
plt.xlabel('Separation (nm)')
plt.ylabel('Force (x10⁻⁵ N/m²)')
plt.title('Casimir Force with and without Metamaterial')
plt.legend()
plt.grid()
plt.savefig('casimir_force_plot.png')
plt.show()
