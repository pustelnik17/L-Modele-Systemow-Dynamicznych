from Solvers import Object, NBodyProblem, Printer

eq = NBodyProblem.SympySolver.getEquations([
    Object(10000000, [0, 0, 0], [0, 0, 0]),
    Object(10000000, [3, 0, 0], [0, 0, 0]),
    Object(10000000, [0, 4, 0], [0, 0, 0]),
])
print(eq[0][0])
sim = NBodyProblem.SympySolver.simulate(eq, 100, 100000)

# fig = plt.figure()
# plt.plot(sim[0][0], "red")
# plt.plot(sim[0][1], "green")
# plt.plot(sim[0][2], "blue")
# plt.show()

# Printer.print(sim)

# for e in eq:
#     for i in range(len(e)):
#         print((e[i].subs("t", 1)))
#     print()