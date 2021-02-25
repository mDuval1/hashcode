import numpy as np
import tqdm


def solve(instance):
    nb_inter = instance['headers']['n_inter']
    inter_to_streets = {i: [] for i in range(nb_inter)}
    streets_to_inter = {}
    streets = instance['streets']
    for street_index, street in streets.items():
        inter = street['end_intersection']
        streets_to_inter[street_index] = inter
        inter_to_streets[inter].append(street_index)
    inter_to_nb_streets = {k: len(v) for k, v in inter_to_streets.items()}

    D = instance['headers']['duration']
    nb_streets = len(streets)
    solution = np.full((D, nb_streets), dtype=bool, fill_value=False)
    # for
    # tirages = np.random.randint(0, nb_streets, size=solution.shape)
    for i in tqdm.tqdm(range(D)):
        for intersection in range(nb_inter):
            nb_streets = inter_to_nb_streets[intersection]
            green = 0
            street = inter_to_streets[intersection][green]
            solution[i, street] = True
    return solution
