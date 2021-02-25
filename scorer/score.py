import tqdm


def score_solution(instance, solution):
    streets = instance['streets']
    duration = instance['headers']['duration']
    streets_dict = {}
    traveling_cars = {}
    streetname_to_street = {}
    street_to_streetname = {}
    for index, st in streets.items():
        name = st['name']
        streetname_to_street[name] = index
        street_to_streetname[index] = name
    for i in range(duration):
        traveling_cars[i] = []
    for street in streets.values():
        streets_dict[street['name']] = []
    for path in instance['paths'].values():
        beginning_street_name = path['names'][0]
        streets_dict[beginning_street_name].append(path['index'])

    scorer = 0

    for t in tqdm.tqdm(range(duration)):
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
                scorer += instance['headers']['bonus'] + (duration - t)
                continue
            next_street_name = instance['paths'][first_car]['names'].pop(0)
            next_street = streetname_to_street[next_street_name]
            traveling_time = t + instance['streets'][next_street]['cross_time']
            if traveling_time >= duration:
                continue
            traveling_cars[traveling_time].append((first_car, next_street))

        for car, street in traveling_cars[t]:
            street_name = street_to_streetname[street]
            streets_dict[street_name].append(car)

    return scorer
