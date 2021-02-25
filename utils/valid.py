"""
Checks the submission is valid
"""
import networkx as nx


def creating_graph(streets):
    G = nx.DiGraph()
    for street in streets.element():
        start = street['start_intersection']
        end = street['end_intersection']
        G.add_edge(start, end)

    return G


def check_validity_T(streets, solution_T):

    G = creating_graph(streets)
    validity = True

    intersections = G.nodes()
    edges = G.out_edges()
    keys_list = list(intersections.keys())
    intersection_key = keys_list.pop()

    while validity and intersection_key:

        intersection = intersections[intersection_key]
        number_of_green_lights = 0
        for street in intersections:
            light = solution_T[street]
            number_of_green_lights += light

        if number_of_green_lights > 1:
            validity = False

        intersection_key = keys_list.pop()

    return validity


def check_validity(instance, solution):
    D = solution.shape[0]
    validity = True
    T = 0

    while validity and T < D:
        validity = check_validity_T(instance['streets'], solution[T])
        T += 1

    return validity


if __name__ == '__main__':
    None
