import numpy as np
import tqdm


def write_solution(path, solution, instance):
    n_inter = instance['headers']['n_inter']
    streets = instance['streets']
    inter_to_streets = {i: [] for i in range(n_inter)}
    streets_to_inter = {}
    streets = instance['streets']
    for street_index, street in streets.items():
        inter = street['end_intersection']
        streets_to_inter[street_index] = inter
        inter_to_streets[inter].append(street_index)
    inters = []
    for inter in tqdm.tqdm(range(n_inter)):
        result = ''
        street_ids = inter_to_streets[inter]
        streets_with_inter = []
        for id_ in street_ids:
            streets_with_inter.append((id_, streets[id_]))
        # streets_with_inter = [
        #     (street_number, street) for street_number, street in streets.items() if inter == street['end_intersection']]
        street_names = []
        for street_number, street in streets_with_inter:
            total = np.sum(solution[:, street_number])
            if total == 0:
                continue
            street_names.append(f'{street["name"]} {total}')
        if len(street_names) == 0:
            continue
        result += f'{inter}\n'
        result += f'{len(street_names)}\n'
        for street_name in street_names:
            result += f'{street_name}\n'
        inters.append(result)

    all_result = ''
    all_result += f'{len(inters)}\n'
    for inter in inters:
        all_result += inter

    with open(path, 'w') as f:
        f.write(all_result)


def write_solutions(solutions, instances):
    for index, (solution, instance) in enumerate(zip(solutions, instances)):
        sol_path = f'./solutions/solution_' + \
            instance['file_path'].split('/')[-1]
        write_solution(sol_path, solution, instance)
