from Solvers import ODEINTMethod, EulerMethod, Printer


def draw():
    def _draw(dt):
        Printer.print(EulerMethod.lorentz, [dt, 25, 1, 1, 1, 10, 8 / 3, 28],
                      f"Lorentz EulerMethod")
        Printer.print(ODEINTMethod.lorentz, [dt, 25, 1, 1, 1, 10, 8 / 3, 28],
                      f"Lorentz ODEINT")
        Printer.print(EulerMethod.lotkaVolterra, [dt, 25, 2, 1, 1.2, 0.6, 0.3, 0.8],
                      f"LotkaVolterra EulerMethod")
        Printer.print(ODEINTMethod.lotkaVolterra, [dt, 25, 2, 1, 1.2, 0.6, 0.3, 0.8],
                      f"LotkaVolterra ODEINT")

    _draw(0.001)
    _draw(0.01)
    _draw(0.02)


def mse():
    def _mse(dt):
        Printer.MSE(EulerMethod.lorentz, ODEINTMethod.lorentz,
                    [dt, 10, 1, 1, 1, 10, 8 / 3, 28])
        Printer.MSE(EulerMethod.lotkaVolterra, ODEINTMethod.lotkaVolterra,
                    [dt, 25, 2, 1, 1.2, 0.6, 0.3, 0.8])

    _mse(0.001)
    _mse(0.01)
    _mse(0.02)


# draw()
mse()
