from Solvers import DynamicModel, Printer


sim1 = DynamicModel.SympySolver.simulate(1, 10, 1, 3, 1, 1, 1, 0.1, 30)
sim2 = DynamicModel.OdeIntSolver.simulate(1, 10, 1, 3, 1, 1, 1, 0.1, 30)
Printer.print(sim1, sim2)
