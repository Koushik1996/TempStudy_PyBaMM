import pybamm as bat
import pandas as pd
import numpy as np

# Setting up the Doyle-Fuller-Newman Model
model = bat.equivalent_circuit.Thevenin(options={"number of rc elements": 1})

# Creating the drive cycle
Data_Loader = bat.DataLoader()
drive_cycle = pd.read_csv(
    f"{Data_Loader.get_data('US06.csv')}", comment="#", header=None
).to_numpy()

# Simulating the DFN Model
sim = bat.Simulation(model)

sim.solve([0, 3600])

sim.plot()