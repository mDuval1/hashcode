import utils.read_instance

ALL_INSTANCES = {
    '0': './instances/00.txt',
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
