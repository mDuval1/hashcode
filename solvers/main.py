import solvers.base
import solvers.naive
import solvers.alea


def solve(instance, solver):
    print('in solve')
    if solver == 'base':
        return solvers.base.solve(instance)
    if solver == 'naive':
        return solvers.naive.solve(instance)
    if solver == 'alea':
        return solvers.alea.solve(instance)
