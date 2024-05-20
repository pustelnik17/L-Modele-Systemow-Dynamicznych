from Solvers import DynamicModel, Printer
from sympy import lambdify

sim1 = DynamicModel.SympySolver.simulate(1, 10, 1, 3, 1, 1, 1, 0.1, 1)
sim2 = DynamicModel.OdeIntSolver.simulate(1, 10, 1, 3, 1, 1, 1, 0.1, 1)
mse = DynamicModel.ErrorCalculator.MSE(sim1, sim2)
mae = DynamicModel.ErrorCalculator.MAE(sim1, sim2)
print(mse)
print(mae)
# Printer.print(sim1, sim2)
