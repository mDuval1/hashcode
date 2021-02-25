"""
Checks the submission is valid
"""
import networkx as nx


def creating_graph(streets):
    G = nx.DiGraph()
    for street in streets.values():
        start = street['start_intersection']
        end = street['end_intersection']
        index = street['index']
        G.add_edge(start, end, index=index)
    return G


def check_validity_T(G, solution_T):

    validity = True

    intersections = list(G.nodes())

    intersection = intersections.pop()

    while validity and intersections:
        number_of_green_lights = 0
        streets_of_intersection = G.in_edges(intersection, data='index')
        for street in streets_of_intersection:
            street_index = street[2]
            light = solution_T[street_index]
            number_of_green_lights += light
        if number_of_green_lights > 1:
            validity = False

        intersection = intersections.pop()

    return validity


def check_validity(instance, solution):
    D = instance['headers']['duration']
    validity = True
    T = 0
    graph = creating_graph(instance['streets'])

    while validity and T < D:
        validity = check_validity_T(graph, solution[T])
        T += 1

    return validity


if __name__ == '__main__':
    instances = {'headers': {'duration': 1, 'n_inter': 4, 'n_streets': 5, 'n_cars': 2, 'bonus': 1000}, 'streets': {0: {'start_intersection': 2, 'end_intersection': 0, 'name': 'rue-de-londres', 'cross_time': 1, 'index': 0}, 1: {'start_intersection': 0, 'end_intersection': 1, 'name': 'rue-d-amsterdam', 'cross_time': 1, 'index': 1}, 2: {'start_intersection': 3, 'end_intersection': 1, 'name': 'rue-d-athenes', 'cross_time': 1, 'index': 2},
                                                                                                                   3: {'start_intersection': 2, 'end_intersection': 3, 'name': 'rue-de-rome', 'cross_time': 2, 'index': 3}, 4: {'start_intersection': 1, 'end_intersection': 2, 'name': 'rue-de-moscou', 'cross_time': 3, 'index': 4}}, 'paths': {0: {'n_streets': 4, 'names': ['rue-de-londres', 'rue-d-amsterdam', 'rue-de-moscou', 'rue-de-rome'], 'index': 0}, 1: {'n_streets': 3, 'names': ['rue-d-athenes', 'rue-de-moscou', 'rue-de-londres'], 'index': 1}}}
    solution = [[0, 0, 0, 0, 0]]

    print(check_validity(instances, solution))
