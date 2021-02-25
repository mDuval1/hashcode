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

    streets = instance['streets']
    streets_dict = {}
    traveling_cars = {}
    streetname_to_street = {}
    street_to_streetname = {}
    for index, st in streets.items():
        name = st['name']
        streetname_to_street[name] = index
        street_to_streetname[index] = name
    for i in range(D):
        traveling_cars[i] = []
    for street in streets.values():
        streets_dict[street['name']] = []
    for path in instance['paths'].values():
        beginning_street_name = path['names'][0]
        streets_dict[beginning_street_name].append(path['index'])

    solution = np.full((D, nb_streets), dtype=bool, fill_value=False)

    for t in tqdm.tqdm(range(D)):
        for intersection in range(nb_inter):
            adjacent_streets = inter_to_streets[intersection]
            nb_waiting_cars = []
            for a_street in adjacent_streets:
                street_name = street_to_streetname[a_street]
                nb_waiting_cars.append(len(streets_dict[street_name]))
            chosen_street = adjacent_streets[np.argmax(
                np.array(nb_waiting_cars))]
            solution[t][chosen_street] = True

        for street in streets.values():
            street_name = street['name']
            has_green_light = solution[t][street['index']]
            if not has_green_light:
                continue
            if len(streets_dict[street_name]) == 0:
                continue
            first_car = streets_dict[street_name].pop(0)
            remaining_streets = instance['paths'][first_car]['names']
            if len(remaining_streets) == 0:
                continue
            next_street_name = instance['paths'][first_car]['names'].pop(0)
            next_street = streetname_to_street[next_street_name]
            traveling_time = t + instance['streets'][next_street]['cross_time']
            if traveling_time >= D:
                continue
            traveling_cars[traveling_time].append((first_car, next_street))

        for car, street in traveling_cars[t]:
            street_name = street_to_streetname[street]
            streets_dict[street_name].append(car)
    print(solution)
    return solution
