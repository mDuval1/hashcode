import click

from read import read_files
from write import write_solutions
from solvers.main import solve
from utils.valid import check_validity
from scorer.score import score_solution


@click.command()
@click.option('--solver', help='Solver to use', required=True, default='base')
@click.option('--instance', required=False, default=None, help='Instances you want to solve, eg: 0-1-4', type=str)
def main(solver, instance):
    print('Reading instances', end='\t')
    instances = read_files(instance)
    print('Done.')
    solutions = []
    for instance in instances:
        print(f'Solving instance {instance["path"]}')
        solutions.append(solve(instance, solver))
    print('Done.')
    print('Checking validity...', end='\t')
    for instance, solution in list(zip(instances, solutions)):
        check_validity(instance, solution)
    print('Done')
    print('Scoring...')
    total_scores = 0
    for instance, solution in list(zip(instances, solutions)):
        total_scores += score_solution(instance, solution)
    print(f'Total scores: {total_scores}')
    print('Writing instances', end='\t')
    instances = write_solutions(solutions, instances)
    print('Done.')


if __name__ == '__main__':
    main()
