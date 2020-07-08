# %%
from IPython import get_ipython

# %% [markdown]
# # Different waves of representing vectors

# %%
from qiskit import *
from qiskit.tools.visualization import plot_bloch_multivector
get_ipython().run_line_magic('matplotlib', 'inline')

# %% [markdown]
# ## Curcuit

# %%
circuit = QuantumCircuit(1,1)
circuit.x(0)
simulator = Aer.get_backend('statevector_simulator')
result = execute(circuit, backend = simulator).result()
statevector = result.get_statevector()
print(statevector)
circuit.draw(output='mpl')

# %% [markdown]
# ## Statevector

# %%
plot_bloch_multivector(statevector)

# %% [markdown]
# ## Histogram

# %%
circuit.measure([0], [0])
backend = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = backend, shots = 1024).result()
counts = result.get_counts()

from qiskit.tools.visualization import plot_histogram
plot_histogram(counts)

# %% [markdown]
# ## Matrix

# %%
circuit = QuantumCircuit(1,1)
circuit.x(0)
simulator = Aer.get_backend('unitary_simulator')
result = execute(circuit, backend = simulator).result()
unitary = result.get_unitary()
print(unitary)