import sympy as sp


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

class Solver:
    @staticmethod
    def nBodyProblem(objects: list):
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
            expression = [(G * objects[j].getMass() * (objects[i].getPos() - objects[j].getPos())) /
                          (_calculateLength((objects[i].getPos() - objects[j].getPos())) ** 3) for j in range(n)]
            iterativeSum = sp.Matrix(sp.Add(*expression))
            equations.append(x[i].diff(t, t) - iterativeSum[0])
            equations.append(y[i].diff(t, t) - iterativeSum[1])
            equations.append(z[i].diff(t, t) - iterativeSum[2])

        icsPosx = {x[i].subs(t, 0): objects[i].getPos()[0] for i in range(n)}
        icsPosy = {y[i].subs(t, 0): objects[i].getPos()[1] for i in range(n)}
        icsPosz = {z[i].subs(t, 0): objects[i].getPos()[2] for i in range(n)}
        icsVelx = {x[i].diff().subs(t, 0): objects[i].getVel()[0] for i in range(n)}
        icsVely = {y[i].diff().subs(t, 0): objects[i].getVel()[1] for i in range(n)}
        icsVelz = {z[i].diff().subs(t, 0): objects[i].getVel()[2] for i in range(n)}

        solutions = sp.dsolve(equations, ics={**icsPosx, **icsPosy, **icsPosz, **icsVelx, **icsVely, **icsVelz})

        return [[solutions[i].rhs, solutions[i + 1].rhs, solutions[i + 2].rhs] for i in range(0, len(solutions), 3)]
