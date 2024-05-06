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

        states = np.empty((num_steps + 1, 3))
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
    def print(f, params):
        result = f(*params)
        if f == ODEINTMethod.lorentz or f == EulerMethod.lorentz:
            fig, ax = plt.subplots(1, 3)
            ax[0].plot(result[:, 0], result[:, 1])
            ax[1].plot(result[:, 1], result[:, 2])
            ax[2].plot(result[:, 2], result[:, 0])
            plt.show()

            fig = plt.figure()
            ax = fig.add_subplot(1, 1, 1, projection='3d')
            ax.plot(result[:, 0],
                    result[:, 1],
                    result[:, 2])
        # else:
        #     num_steps = int(params[1] / params[0])
        #     fig, ax = plt.subplots(1, 1)
        #     ax[0].plot(result[:, 0], result[:, 0])
        #     ax[0].plot(result[:, 1], result[:, 1])
        #     plt.show()
        plt.show()
