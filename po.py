import streamlit  as st
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import scipy.constants as const
#Give header
st.title("LET'S DIVE IN QUANTUM WORLD!")
st.markdown("**_I do not like it, and I am sorry I ever had anything to do with it_**  ____~ **Erwin Schrodinger** ")                                                                     
st.header("WAVE FUNCTION AND PROBABLITY DENSITY OF 1D POTENTIAL ")

# Define the Streamlit slider to adjust the potential well width and depth
L_slider = st.sidebar.slider('Width of the potential well (nm)', 1, 100, 10, 1)
V_slider = st.sidebar.slider('Depth of the potential well (eV)', 0.1, 10.0, 1.0, 0.1)

# Define the range of x values to calculate the wavefunction
L = L_slider * 1e-9
V = V_slider * 1.6e-19
x_range = np.linspace(0, L, 100)
dx = x_range[1] - x_range[0]

# Calculate the wavefunctions and energies of the particle
hbar = const.hbar
n_max = 10
energies = [(n*2 * np.pi*2 * (hbar*2)/(2 * L*2))/(1.6e-19) for n in range(1, n_max+1)]
wavefunctions = [np.sqrt(2/L) * np.sin(n * np.pi * x_range / L) for n in range(1, n_max+1)]

# Define the Streamlit dropdown to select which energy level to display
energy_level = st.sidebar.selectbox('Select an energy level', range(1, n_max+1))

# Calculate the probability density for the selected energy level
n = energy_level - 1
psi = wavefunctions[n]
prob_density = np.abs(psi)**2

# Plot the wavefunction and probability density for the selected state
fig = plt.figure(figsize=(12, 5))

# Plot the wavefunction
ax1 = fig.add_subplot(121)
ax1.plot(x_range, psi, color='blue', label='Wavefunction')
ax1.set_xlabel('x (m)')
ax1.set_ylabel('psi')
ax1.set_title(f'Wavefunction of the particle in state {n+1}')
ax1.legend()

# Plot the probability density
ax2 = fig.add_subplot(122)
ax2.plot(x_range, prob_density, color='red', label='Probability density')
ax2.set_xlabel('x (m)')
ax2.set_ylabel('|psi|^2')
ax2.set_title(f'Probability density of the particle in state {n+1}')
ax2.legend()

# Display the graph
st.pyplot(fig)
