from Solvers import Object, Solver

sim = Solver.nBodyProblem([Object(1, [0, 0, 0], [10, 9, 8]), Object(2, [1, 1, 1])])
for e in sim:
    print(e)
