from os import set_blocking


def process_street(street, i):
    prms = street.split(' ')
    return {
        'start_intersection': int(prms[0]),
        'end_intersection': int(prms[1]),
        'name': prms[2],
        'cross_time': int(prms[3].split('\n')[0]),
        'index': i
    }


def process_path(path, i):
    prms = path.split(' ')
    streets = prms[1:-1]
    streets.append(prms[-1].split('\n')[0])
    return {
        'n_streets': int(prms[0]),
        'names': streets,
        'index': i
    }


def read_instance(path):
    with open(path, 'r') as f:
        file = f.readlines()
    headers = list(map(int, file[0].split(' ')))
    D, I, S, V, F = headers
    streets = file[1:S+1]
    paths = file[S+1:S+1+V]
    streets_processed = {}
    for i, street in enumerate(streets):
        streets_processed[i] = process_street(street, i)
    paths_processed = {}
    for i, path in enumerate(paths):
        paths_processed[i] = process_path(path, i)
    instance = {
        'headers': {
            'duration': D,
            'n_inter': I,
            'n_streets': S,
            'n_cars': V,
            'bonus': F
        },
        'streets': streets_processed,
        'paths': paths_processed
    }
    return instance


def read_instance_base(path):
    with open(path, 'r') as f:
        file = f.readlines()
    return file
