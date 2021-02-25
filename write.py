import numpy as np


def write_solution(path, solution, instance):
    n_inter = instance['headers']['n_inter']
    streets = instance['streets']
    result = ''
    for inter in range(n_inter):
        result += f'{inter}\n'
        streets_with_inter = [
            (street_number, street) for street_number, street in streets.items() if inter == street['end_intersection']]
        street_names = []
        for street_number, street in streets_with_inter:
            total = np.sum(solution[:, street_number])
            street_names.append(f'{street["name"]} {total}')
        result += f'{len(street_names)}\n'
        for street_name in street_names:
            result += f'{street_name}\n'

    print(result)
    with open(path, 'w') as f:
        f.write(result)


def write_solutions(solutions, instances):
    for index, (solution, instance) in enumerate(zip(solutions, instances)):
        # instance_path = instance['path'].split('/')[-1]
        sol_path = './solutions/solution' + str(index)
        write_solution(sol_path, solution, instance)
