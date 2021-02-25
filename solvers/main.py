import solvers.base


def solve(instance, solver):
    if solver == 'base':
        return solvers.base.solve(instance)
