import solvers.base
import solvers.naive


def solve(instance, solver):
    print('in solve')
    if solver == 'base':
        return solvers.base.solve(instance)
    if solver == 'naive':
        return solvers.naive.solve(instance)
