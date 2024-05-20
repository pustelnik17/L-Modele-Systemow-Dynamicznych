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

    class ErrorCalculator:
        @staticmethod
        def MAE(tseries1, tseries2):
            summation = 0
            for i in range(len(tseries1[0])):
                summation += (abs(tseries1[0][i] - tseries2[0][i]).evalf(5) +
                              abs(tseries1[1][i] - tseries2[1][i]).evalf(5))
            return summation/len(tseries1[0])

        @staticmethod
        def MAEplot(tseries1, tseries2):
            result = [(abs(tseries1[0][i] - tseries2[0][i]) + abs(tseries1[1][i] - tseries2[1][i])).evalf(3)
                      for i in range(len(tseries1[0]))]
            for i in range(1, len(tseries1[0])):
                result[i] += result[i - 1]
            for i in range(1, len(tseries1[0])):
                result[i] /= i
            return result

        @staticmethod
        def MSE(tseries1, tseries2):
            summation = 0
            for i in range(len(tseries1[0])):
                summation += (((tseries1[0][i] - tseries2[0][i]) ** 2).evalf(5) +
                              ((tseries1[1][i] - tseries2[1][i]) ** 2).evalf(5))
            return summation/len(tseries1[0])

        @staticmethod
        def MSEplot(tseries1, tseries2):
            result = [((tseries1[0][i] - tseries2[0][i]) ** 2 + (tseries1[1][i] - tseries2[1][i]) ** 2).evalf(3)
                      for i in range(len(tseries1[0]))]
            for i in range(1, len(tseries1[0])):
                result[i] += result[i - 1]
            for i in range(1, len(tseries1[0])):
                result[i] /= i
            return result


class Printer:
    @staticmethod
    def signal(systemEvolution1, systemEvolution2, dt):
        fig, ax = plt.subplots(1, 2)
        fig.suptitle(f"Układ RLC | dt = {dt}", fontsize="x-large")

        ymin, ymax = (min(*systemEvolution1[0], *systemEvolution1[1], *systemEvolution2[0], *systemEvolution2[1]),
                      max(*systemEvolution1[0], *systemEvolution1[1], *systemEvolution2[0], *systemEvolution2[1]))

        ax[0].set_ylim([ymin, ymax])
        ax[1].set_ylim([ymin, ymax])

        ax[0].plot(systemEvolution1[0], "red", label="SYMPY Q(t)")
        ax[0].plot(systemEvolution1[1], "blue", label="SYMPY I(t)")
        ax[1].plot(systemEvolution2[0], "darkred", label="ODEINT Q(t)")
        ax[1].plot(systemEvolution2[1], "cornflowerblue", label="ODEINT I(t)")

        ticks = np.linspace(0, len(systemEvolution1[0]), 5)
        ax[0].set_xticks(ticks)
        ax[0].set_xticklabels(np.round(ticks / (1 / dt)))
        ax[1].set_xticks(ticks)
        ax[1].set_xticklabels(np.round(ticks / (1 / dt)))

        lines_labels = [ax.get_legend_handles_labels() for ax in fig.axes]
        lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
        fig.legend(lines, labels)
        plt.show()

    @staticmethod
    def dependency(systemEvolution1, systemEvolution2, dt):
        fig, ax = plt.subplots(1, 2)
        fig.suptitle(f"Układ RLC | dt = {dt}", fontsize="x-large")

        ymin, ymax = (min(*systemEvolution1[0], *systemEvolution1[1], *systemEvolution2[0], *systemEvolution2[1]),
                      max(*systemEvolution1[0], *systemEvolution1[1], *systemEvolution2[0], *systemEvolution2[1]))

        ax[0].set_ylim([ymin, ymax])
        ax[1].set_ylim([ymin, ymax])

        ax[0].plot(systemEvolution1[0], systemEvolution1[1], "red", label="SYMPY Q(I)")
        ax[1].plot(systemEvolution2[0], systemEvolution2[1], "darkred", label="ODEINT Q(I)")

        lines_labels = [ax.get_legend_handles_labels() for ax in fig.axes]
        lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
        fig.legend(lines, labels)

        plt.show()
