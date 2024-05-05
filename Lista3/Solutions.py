from Solvers import ODEINTMethod, EulerMethod
import matplotlib.pyplot as plt


# print(EulerMethod.LotkaVolterra(0.01, 10, 2, 1, 1.2, 0.6, 0.3, 0.8))
print(EulerMethod.lorentz(0.01, 10, 1, 1, 1, 10, 8/3, 28))
result = ODEINTMethod.lorentz(0.01, 25, 1, 1, 1, 10, 8/3, 28)
print(result)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(result[:, 0], result[:, 1])

# ax = fig.add_subplot(1, 1, 1, projection='3d')
# ax.plot(result[:, 0],
#         result[:, 1],
#         result[:, 2])
# ax.set_title("odeint")
plt.show()
