

def score_solution(instance, solution):
    ds = solution['deliveries']
    pizzas = instance['pizzas']
    total = 0
    for d in ds:
        d_pizzas = d['pizzas']
        ingredients = []
        for id_ in d_pizzas:
            ingredients.extend(pizzas[id_]['ingredients'])
        n_ing = len(set(ingredients))
        total += n_ing**2
    print('Score for instance {0} : {1}'.format(instance['path'], total))
    return total
