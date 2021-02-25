

def write_solution(path, solution):
    with open(path, 'w') as f:
        f.write(str(solution['n_d']) + '\n')
        for d in solution['deliveries']:
            output_d = str(d['team_size']) + ' ' + \
                ' '.join(list(map(str, d['pizzas']))) + '\n'
            f.write(output_d)


def write_solutions(solutions, instances):
    for solution, instance in zip(solutions, instances):
        instance_path = instance['path'].split('/')[-1]
        sol_path = './solutions/solution' + instance_path
        write_solution(sol_path, solution)
