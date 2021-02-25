"""
Checks the submission is valid
"""


def check_validity(instance, solution):
    if solution['n_d'] > instance['headers']['n_pizzas']:
        raise Exception('Number of deliveries exceeds number of pizzas')
    if solution['n_d'] != len(solution['deliveries']):
        raise Exception('Inconsistency in solution')
    for team_size in [2, 3, 4]:
        teams = instance['headers'][f't_{team_size}']
        d_to_size = 0
        for d in solution['deliveries']:
            if d['team_size'] == team_size:
                d_to_size += 1
        if teams < d_to_size:
            raise Exception(f'Inconsistency in solution team_size {team_size}')
    n_pizzas = instance['headers']['n_pizzas']
    delivered = dict(zip(list(range(n_pizzas)), [False]*n_pizzas))
    for i, d in enumerate(solution['deliveries']):
        for pizza in d['pizzas']:
            if not delivered[pizza]:
                delivered[pizza] = True
            else:
                raise Exception(
                    f'Pizza {pizza} already delivered, delivery {i}')
    for i, d in enumerate(solution['deliveries']):
        if d['team_size'] != len(d['pizzas']):
            raise Exception(
                f'All members of the team should receive a pizza delivery {i}, pizzas {d["pizzas"]}, team size {d["team_size"]}')
