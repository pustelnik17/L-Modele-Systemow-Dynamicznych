from typing import Tuple, List, Union, Any

import numpy
import numpy as np


class EulerMethod:
    @staticmethod
    def Lorentz(dt: float, T: float,  x: float, y: float, z: float, s: float, b: float, p: float):
        xVec, yVec, zVec = [x], [y], [z]
        for step in range(int(T / dt)):
            xVec.append(xVec[step] + s*(yVec[step] - xVec[step]))
            yVec.append(yVec[step] + xVec[step]*(p - xVec[step]) - yVec[step])
            zVec.append(zVec[step] + xVec[step]*yVec[step] - b*zVec[step])
        return xVec, yVec, zVec

    @staticmethod
    def LotkaVolterra(dt: float, T: float, x: float, y: float, a: float, b: float, c: float, d: float)\
            -> tuple[list[Union[float, Any]], list[Union[float, Any]]]:
        prey, predators = [x], [y]
        for step in range(int(T/dt)):
            prey.append(prey[step] + (a - b * predators[step]) * prey[step] * dt)
            predators.append(predators[step] + (c * prey[step] - d) * predators[step] * dt)
        return prey, predators


class ODESolver:
    @staticmethod
    def Lorentz(s: float = 10, b: float = 8 / 3, p: float = 28):
        pass

    @staticmethod
    def LotkaVolterra(x: float = 2, y: float = 1, a: float = 1.2, b: float = 0.6, c: float = 0.3, d: float = 0.8):
        pass
