# %%
from IPython import get_ipython


# %%
from qiskit import *
get_ipython().run_line_magic('matplotlib', 'inline')


# %%
qr = QuantumRegister(2)
cr = ClassicalRegister(2)
circuit = QuantumCircuit(qr, cr)

circuit.draw()


# %%
circuit.h(qr[0])
circuit.cx(qr[0], qr[1])
circuit.measure(qr, cr)
circuit.draw(output='mpl')

# %% [markdown]
# # Simulating the code in this (classical) computer

# %%
simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = simulator).result()

from qiskit.tools.visualization import plot_histogram
plot_histogram(result.get_counts(circuit))

# %% [markdown]
# # Running the code in a Quantum Computer

# %%
IBMQ.load_account()


# %%
provider = IBMQ.get_provider('ibm-q')
qcomp = provider.get_backend('ibmq_16_melbourne')

job = execute(circuit, backend=qcomp)
from qiskit.tools.monitor import job_monitor
job_monitor(job)


# %%
result = job.result()
plot_histogram(result.get_counts(circuit))