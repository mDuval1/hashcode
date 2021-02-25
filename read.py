import utils.read_instance

ALL_INSTANCES = {
    '0': './instances/a.txt',
    '1': './instances/b.txt',
    '2': './instances/c.txt',
    '3': './instances/d.txt',
    '4': './instances/e.txt',
    '5': './instances/f.txt',
}


instance = {
    'headers': {
        'duration': 10,
        'n_inter': 5,
        'n_streets': 5,
        'n_cars': 10,
        'bonus': 100
    },
    'streets': [
        {
            'start_intersection': 1,
            'end_intersection': 2,
            'name': 'blabla',
            'cross_time': 5
        }
    ],
    'paths': [
        {
            'n_streets': 3,
            'names': ['blabla']
        }
    ]
}


def select_files(instances):
    if instances is None:
        return list(ALL_INSTANCES.values())
    else:
        instance_ids = instances.split('-')
        return [ALL_INSTANCES[i] for i in instance_ids]


def read_files(instances):
    file_paths = select_files(instances)
    files = []
    for file_path in file_paths:
        files.append(utils.read_instance.read_instance(file_path))
    return files
