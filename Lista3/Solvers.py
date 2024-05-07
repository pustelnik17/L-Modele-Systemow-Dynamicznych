import itertools
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


class EulerMethod:
    @staticmethod
    def lorentz(dt: float, t: float, x0: float, y0: float, z0: float, sigma: float, beta: float, rho: float):
        def _lorentz(state):
            x, y, z = state
            dx = sigma * (y - x)
            dy = rho * x - y - x * z
            dz = x * y - beta * z
            return np.array([dx, dy, dz])

        num_steps = int(t / dt)

        states = np.empty((num_steps + 1, 3))
        states[0] = (x0, y0, z0)
        for i in range(num_steps):
            states[i + 1] = states[i] + _lorentz(states[i]) * dt
        return states

    @staticmethod
    def lotkaVolterra(dt: float, t: float, x0: float, y0: float, a: float, b: float, c: float, d: float):
        def _lotkaVolterra(state):
            x, y = state

            dx = (a - b * y) * x
            dy = (c * x - d) * y

            return np.array([dx, dy])

        num_steps = int(t / dt)

        states = np.empty((num_steps + 1, 2))
        states[0] = (x0, y0)
        for i in range(num_steps):
            states[i + 1] = states[i] + _lotkaVolterra(states[i]) * dt
        return states

class ODEINTMethod:

    @staticmethod
    def lorentz(dt: float, t: float, x0: float, y0: float, z0: float, sigma: float, beta: float, rho: float):
        def _lorenz(state, _t, _sigma, _beta, _rho):
            x, y, z = state

            dx = _sigma * (y - x)
            dy = x * (_rho - z) - y
            dz = x * y - _beta * z

            return [dx, dy, dz]

        args = (x0, y0, z0)
        time = np.arange(0.0, t, dt)
        param = (sigma, beta, rho)
        return odeint(_lorenz, args, time, param)

    @staticmethod
    def lotkaVolterra(dt: float, t: float, x0: float, y0: float, a: float, b: float, c: float, d: float):
        def _lotkaVolterra(state, _t, _a, _b, _c, _d) -> list:
            x, y = state

            dx = (_a - _b * y) * x
            dy = (_c * x - _d) * y

            return [dx, dy]

        args = (x0, y0)
        time = np.arange(0.0, t, dt)
        param = (a, b, c, d)
        return odeint(_lotkaVolterra, args, time, param)


class Printer:
    @staticmethod
    def print(f, params, saveName=None):
        result = f(*params)

        # signal plot
        time = np.arange(0, len(result))
        fig, ax = plt.subplots()
        for var in range(len(result[0])):
            ax.plot(time, result[:, var])
        plt.title(f.__name__.title() + f"  dt={params[0]}")
        ticks = np.linspace(0, len(result), 5)
        ax.set_xticks(ticks)
        ax.set_xticklabels(ticks/100)
        if saveName is not None:
            plt.savefig("Images/" + saveName + f"/signal/{params[0]}.png")
        else:
            plt.show()
        plt.close(fig)

        # signal dependency plot
        indexLst = [var for var in range(len(result[1]))]
        indexComb = list(itertools.combinations(indexLst, 2))
        fig, ax = plt.subplots(1, len(indexComb))
        if len(indexComb) == 1:
            ax.plot(result[:, indexComb[0][0]], result[:, indexComb[0][1]], 'blue')
        else:
            for var in range(len(indexComb)):
                ax[var].plot(result[:, indexComb[var][0]], result[:, indexComb[var][1]], 'blue')
        if saveName is not None:
            plt.savefig("Images/" + saveName + f"/dependency/{params[0]}.png")
        else:
            plt.show()
        plt.close(fig)

        # 3d signal dependancy plot
        if len(indexComb) == 3:
            fig = plt.figure()
            ax = plt.axes(projection='3d')
            ax.plot3D(*result.T, 'blue')
            if saveName is not None:
                plt.savefig("Images/" + saveName + f"/3d/{params[0]}.png")
            else:
                plt.show()
            plt.close(fig)
