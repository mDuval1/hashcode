import solvers.base
import solvers.naive
import solvers.alea
import solvers.clever
import solvers.clever_faster


def solve(instance, solver):
    print('in solve')
    if solver == 'base':
        return solvers.base.solve(instance)
    if solver == 'naive':
        return solvers.naive.solve(instance)
    if solver == 'alea':
        return solvers.alea.solve(instance)
    if solver == 'clever':
        return solvers.clever.solve(instance)
    if solver == 'cleverfaster':
        return solvers.clever_faster.solve(instance)
