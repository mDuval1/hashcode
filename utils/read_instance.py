from os import set_blocking


def process_pizza(pizza, i):
    prms = pizza.split(' ')
    return {'id': i, 'n_ingre': int(prms[0]), 'ingredients': prms[1:-1]}


def read_instance(path):
    with open(path, 'r') as f:
        file = f.readlines()
    headers = list(map(int, file[0].split(' ')[:-1]))
    pizzas = file[1:]
    pizzas_processed = {}
    for i, pizza in enumerate(pizzas):
        pizzas_processed[i] = process_pizza(pizza, i)
    instance = {
        'headers': {
            'n_pizzas': headers[0],
            't_2': headers[1],
            't_3': headers[2],
            't_4': headers[3]
        },
        'pizzas': pizzas_processed,
        'path': path
    }
    return instance


def read_instance_base(path):
    with open(path, 'r') as f:
        file = f.readlines()
    return file
