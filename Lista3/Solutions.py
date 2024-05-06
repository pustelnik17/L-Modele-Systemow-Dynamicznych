from Solvers import ODEINTMethod, EulerMethod, Printer


Printer.print(EulerMethod.lorentz, [0.01, 25, 1, 1, 1, 10, 8/3, 28])
Printer.print(ODEINTMethod.lorentz, [0.01, 25, 1, 1, 1, 10, 8/3, 28])
Printer.print(ODEINTMethod.lotkaVolterra, [0.01, 10, 2, 1, 1.2, 0.6, 0.3, 0.8])
