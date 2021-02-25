

def score_solution(instance, solution):
    streets = instance['streets']
    duration = instance['headers']['duration']
    streets_dict = {}
    traveling_cars = {}
    for i in range(duration):
        traveling_cars[i] = []
    for street in streets:
        streets_dict[street['name']] = []
    for path in instance['paths']:
        beginning_street_name = path['names'][0]
        streets_dict[beginning_street_name].append(path['index'])

    scorer = 0

    for t in range(duration):
        for street in streets:
            street_name = street['name']
            has_green_light = solution[t][street['index']]
            if not has_green_light:
                continue
            first_car = streets_dict[street_name].pop(0)
            remaining_streets = instance['paths'][first_car]['names']
            if len(remaining_streets) == 0:
                scorer += instance['headers']['bonus'] + (duration - t)
                continue
            instance['paths'][first_car]['names'].pop(0)
            next_street = instance['paths'][first_car]['names'][0]

            traveling_time = t + instance['streets'][next_street]['cross_time']
            traveling_cars[traveling_time].append((first_car, next_street))

            for car, street in traveling_cars[t]:
                streets_dict[street].append(car)

    return scorer
