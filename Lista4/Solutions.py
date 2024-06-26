from Solvers import DynamicModel, Printer, np
import matplotlib.pyplot as plt


# 1, 10, 1, 3, 1, 1, 1, dt, 20
# MSE:  10.165  MAE:  3.3094
# MSE:  10.196  MAE:  3.3683
# MSE:  10.208  MAE:  3.3887

# 1, 3, 2, 3, 1, 3, 6, dt, 20
# MSE:  0.54235  MAE:  0.80282
# MSE:  0.57134  MAE:  0.82821
# MSE:  0.57044  MAE:  0.82354

# 1, 10, 1, 3, 1, 1, 8, dt, 30
# MSE:  6.6868  MAE:  2.3618
# MSE:  6.7092  MAE:  2.3761
# MSE:  6.7096  MAE:  2.3825

def runSimulation(dt: float):
    sim1 = DynamicModel.SympySolver.simulate(1, 10, 1, 3, 1, 1, 8, dt, 30)
    sim2 = DynamicModel.OdeIntSolver.simulate(1, 10, 1, 3, 1, 1, 8, dt, 30)
    Printer.signal(sim1, sim2, dt)
    Printer.dependency(sim1, sim2, dt)

    mse = DynamicModel.ErrorCalculator.MSE(sim1, sim2)
    mae = DynamicModel.ErrorCalculator.MAE(sim1, sim2)
    print("MSE: ", mse, " MAE: ", mae)

    maeT = DynamicModel.ErrorCalculator.MAEplot(sim1, sim2)
    mseT = DynamicModel.ErrorCalculator.MSEplot(sim1, sim2)
    fig, ax = plt.subplots(1, 1)
    fig.suptitle(f"Układ RLC - Error chart | dt = {dt}", fontsize="x-large")
    ax.plot(maeT, "red", label="MAE")
    ax.plot(mseT, "blue", label="MSE")
    ticks = np.linspace(0, len(maeT), 5)
    ax.set_xticks(ticks)
    ax.set_xticklabels(np.round(ticks / (1 / dt)))
    plt.legend()
    plt.show()


runSimulation(1)
runSimulation(0.5)
runSimulation(0.1)
