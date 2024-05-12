import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Object:
    def __init__(self, mass, position=None, velocity=None):
        if velocity is None:
            velocity = [0, 0, 0]
        if position is None:
            position = [0, 0, 0]
        self.mass = mass
        self.pos = sp.Matrix(position)
        self.vel = sp.Matrix(velocity)

    def getMass(self):
        return self.mass

    def getPos(self):
        return self.pos

    def getVel(self):
        return self.vel


class NBodyProblem:
    class SympySolver:
        @staticmethod
        def getEquations(objects: list) -> list[tuple]:
            def _calculateLength(m: sp.Matrix):
                sumT = 0
                for k in range(len(m)):
                    sumT += m[k] * m[k]
                return sp.sqrt(sumT)

            n = len(objects)
            G = sp.symbols('G')
            t = sp.symbols('t')

            x, y, z = [], [], []
            for i in range(n):
                x.append(sp.Function(f"x{i}")(t))
                y.append(sp.Function(f"y{i}")(t))
                z.append(sp.Function(f"z{i}")(t))

            equations = []
            for i in range(n):
                expression = [(objects[j].getMass() * (objects[i].getPos() - objects[j].getPos())) /
                              (_calculateLength((objects[i].getPos() - objects[j].getPos())) ** 3) for j in range(n)]
                iterativeSum = sp.Matrix(sp.Add(*expression))
                equations.append(x[i].diff(t, t) - G * iterativeSum[0])
                equations.append(y[i].diff(t, t) - G * iterativeSum[1])
                equations.append(z[i].diff(t, t) - G * iterativeSum[2])

            ics = {
                **{axis[0][i].subs(t, 0): objects[i].getPos()[axis[1]]
                   for i in range(n) for axis in ((x, 0), (y, 1), (z, 2))},
                **{axis[0][i].diff().subs(t, 0): objects[i].getVel()[axis[1]]
                   for i in range(n) for axis in ((x, 0), (y, 1), (z, 2))}
            }

            solutions = sp.dsolve(equations, ics=ics)

            return [(solutions[i].rhs.subs("G", 6.67430 * (10 ** -11)),
                     solutions[i + 1].rhs.subs("G", 6.67430 * (10 ** -11)),
                     solutions[i + 2].rhs.subs("G", 6.67430 * (10 ** -11)))
                    for i in range(0, len(solutions), 3)]

        @staticmethod
        def simulate(equations: list[tuple], dt: float, time: float):
            numberOfSteps = int(time / dt)
            systemEvolution = []
            for obj in equations:
                objEvolution = []
                for axis in range(len(obj)):
                    axisEvolution = []
                    for step in range(numberOfSteps):
                        axisEvolution.append(obj[axis].subs("t", dt*step))
                    objEvolution.append(axisEvolution)
                systemEvolution.append(objEvolution)
            return systemEvolution

class Printer:
    @staticmethod
    def print(systemEvolution):
        # fig = plt.figure()
        # fig.suptitle(f"N Body Problem", fontsize="x-large")
        # ax = plt.axes(projection='3d')
        # for obj in systemEvolution:
        #     ax.plot3D(obj[0], obj[1], obj[2])
        #     ax.scatter(obj[0][0], obj[1][0], obj[2][0], c='red', marker='*', s=10)
        # plt.show()

        def update(frame):
            scat.set_offsets([systemEvolution[0][0][frame], systemEvolution[1][0][frame]])

            return scat,

            # Inicjalizacja wykresu

        fig, ax = plt.subplots()
        x = 30000
        ax.set_xlim(-2*x, 0)  # Ustawienie limitów osi x
        ax.set_ylim(0, 2*x)  # Ustawienie limitów osi y

        # Inicjalizacja obiektu punktu
        scat = ax.scatter(systemEvolution[0][0][0], systemEvolution[0][1][0])

        # Ustawienie animacji
        ani = animation.FuncAnimation(fig, update, frames=len(systemEvolution[0][0]), interval=50, blit=True)

        # Wyświetlenie animacji
        plt.show()
