from typing import Tuple, Any

import sympy as sp
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


class DynamicModel:
    class SympySolver:
        @staticmethod
        def RLC(q0: float, i0: float, R: float, L: float, C: float, A: float, Omega: float):
            t = sp.symbols('t')
            q = sp.Function('q')(t)
            i = sp.Function('i')(t)

            eq1 = sp.Eq(q.diff(t), i)
            eq2 = sp.Eq(L * i.diff(t) + R * i + q / C, A * sp.cos(Omega * t))

            solution = sp.dsolve((eq1, eq2), ics={q.subs(t, 0): q0, i.subs(t, 0): i0})

            return solution

        @staticmethod
        def simulate(q0: float, i0: float, R: float, L: float, C: float, A: float, Omega: float, dt: float,
                     time: float):
            equations: list[sp.Eq] = DynamicModel.SympySolver.RLC(q0, i0, R, C, L, A, Omega)
            numberOfSteps = int(time / dt)
            systemEvolution = []
            for equation in equations:
                eqEvolution = []
                for step in range(numberOfSteps):
                    eqEvolution.append(equation.rhs.subs("t", dt * step))
                systemEvolution.append(eqEvolution)
            return systemEvolution

    class OdeIntSolver:
        @staticmethod
        def simulate(q0: float, i0: float, R: float, L: float, C: float, A: float, Omega: float, dt: float,
                     time: float):
            def _V(_t, a: float, omega: float):
                return a * np.cos(omega * _t)

            def _RLC(y, _t, _R, _L, _C):
                q, i = y

                dqdt = i
                didt = (1 / _L) * (_V(_t, A, Omega) - _R * i - q / _C)

                return [dqdt, didt]

            y0 = [q0, i0]
            t = np.arange(0.0, time, dt)
            solution = odeint(_RLC, y0, t, args=(R, L, C))
            return solution.T


class Printer:
    @staticmethod
    def print(systemEvolution1, systemEvolution2):
        fig, ax = plt.subplots(1, 2)
        fig.suptitle(f"Układ RLC", fontsize="x-large")

        ymin, ymax = (min(*systemEvolution1[0], *systemEvolution1[1], *systemEvolution2[0], *systemEvolution2[1]),
                      max(*systemEvolution1[0], *systemEvolution1[1], *systemEvolution2[0], *systemEvolution2[1]))

        ax[0].set_ylim([ymin, ymax])
        ax[1].set_ylim([ymin, ymax])

        ax[0].plot(systemEvolution1[0], "red", label="Q(t)")
        ax[0].plot(systemEvolution1[1], "blue", label="I(t)")
        ax[1].plot(systemEvolution2[0], "darkred", label="Q(t)")
        ax[1].plot(systemEvolution2[1], "cornflowerblue", label="I(t)")

        plt.legend()
        plt.show()
