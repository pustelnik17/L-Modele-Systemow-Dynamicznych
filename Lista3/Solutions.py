from Solvers import ODEINTMethod, EulerMethod, Printer

dt = 0.01
Printer.print(EulerMethod.lorentz, [dt, 25, 1, 1, 1, 10, 8/3, 28],
              f"Lorentz EulerMethod {dt}")
Printer.print(ODEINTMethod.lorentz, [dt, 25, 1, 1, 1, 10, 8/3, 28],
              f"Lorentz ODEINT {dt}")
Printer.print(EulerMethod.lotkaVolterra, [dt, 25, 2, 1, 1.2, 0.6, 0.3, 0.8],
              f"LotkaVolterra EulerMethod {dt}")
Printer.print(ODEINTMethod.lotkaVolterra, [dt, 25, 2, 1, 1.2, 0.6, 0.3, 0.8],
              f"LotkaVolterra ODEINT {dt}")
dt = 0.02
Printer.print(EulerMethod.lorentz, [dt, 25, 1, 1, 1, 10, 8/3, 28],
              f"Lorentz EulerMethod {dt}")
Printer.print(ODEINTMethod.lorentz, [dt, 25, 1, 1, 1, 10, 8/3, 28],
              f"Lorentz ODEINT {dt}")
Printer.print(EulerMethod.lotkaVolterra, [dt, 25, 2, 1, 1.2, 0.6, 0.3, 0.8],
              f"LotkaVolterra EulerMethod {dt}")
Printer.print(ODEINTMethod.lotkaVolterra, [dt, 25, 2, 1, 1.2, 0.6, 0.3, 0.8],
              f"LotkaVolterra ODEINT {dt}")
dt = 0.001
Printer.print(EulerMethod.lorentz, [dt, 25, 1, 1, 1, 10, 8/3, 28],
              f"Lorentz EulerMethod {dt}")
Printer.print(ODEINTMethod.lorentz, [dt, 25, 1, 1, 1, 10, 8/3, 28],
              f"Lorentz ODEINT {dt}")
Printer.print(EulerMethod.lotkaVolterra, [dt, 25, 2, 1, 1.2, 0.6, 0.3, 0.8],
              f"LotkaVolterra EulerMethod {dt}")
Printer.print(ODEINTMethod.lotkaVolterra, [dt, 25, 2, 1, 1.2, 0.6, 0.3, 0.8],
              f"LotkaVolterra ODEINT {dt}")
dt = 0.001
Printer.print(EulerMethod.lorentz, [dt, 25, 1, 1, 1, 10, 8/3, 28],
              f"Lorentz EulerMethod dt={dt}")
Printer.print(ODEINTMethod.lorentz, [dt, 25, 1, 1, 1, 10, 8/3, 28],
              f"Lorentz ODEINT {dt}")
Printer.print(EulerMethod.lotkaVolterra, [dt, 25, 2, 1, 1.2, 0.6, 0.3, 0.8],
              f"LotkaVolterra EulerMethod {dt}")
Printer.print(ODEINTMethod.lotkaVolterra, [dt, 25, 2, 1, 1.2, 0.6, 0.3, 0.8],
              f"LotkaVolterra ODEINT {dt}")