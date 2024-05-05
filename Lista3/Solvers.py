from typing import Union, Any
import numpy as np
from scipy.integrate import odeint

class EulerMethod:
    @staticmethod
    def lorentz(dt: float, T: float,  x: float, y: float, z: float, s: float, b: float, p: float):
        xVec, yVec, zVec = [x], [y], [z]
        for step in range(int(T / dt)):
            xVec.append(xVec[step] + s*(yVec[step] - xVec[step]))
            yVec.append(yVec[step] + xVec[step]*(p - xVec[step]) - yVec[step])
            zVec.append(zVec[step] + xVec[step]*yVec[step] - b*zVec[step])
        return xVec, yVec, zVec

    @staticmethod
    def lotkaVolterra(dt: float, T: float, x: float, y: float, a: float, b: float, c: float, d: float)\
            -> tuple[list[Union[float, Any]], list[Union[float, Any]]]:
        prey, predators = [x], [y]
        for step in range(int(T/dt)):
            prey.append(prey[step] + (a - b * predators[step]) * prey[step] * dt)
            predators.append(predators[step] + (c * prey[step] - d) * predators[step] * dt)
        return prey, predators


class ODEINTMethod:

    @staticmethod
    def lorentz(dt: float, t: float, x0: float, y0: float, z0: float, sigma: float, beta: float, rho: float):
        def _lorenz(state, t, sigma, beta, rho):
            x, y, z = state

            dx = sigma * (y - x)
            dy = x * (rho - z) - y
            dz = x * y - beta * z

            return [dx, dy, dz]

        args = (x0, y0, z0)
        time = np.arange(0.0, t, dt)
        param = (sigma, beta, rho)
        return odeint(_lorenz, args, time, param)

    @staticmethod
    def lotkaVolterra(dt: float, t: float, x0: float, y0: float, a: float, b: float, c: float, d: float):
        def _lotkaVolterra(state, t, a, b, c, d) -> list:
            x, y = state

            dx = (a-b*y)*x
            dy = (c*x-d)*y

            return [dx, dy]

        args = (x0, y0)
        time = np.arange(0.0, t, dt)
        param = (a, b, c, d)
        return odeint(_lotkaVolterra, args, time, param)
