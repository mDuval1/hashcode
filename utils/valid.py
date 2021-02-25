"""
Checks the submission is valid
"""
import networkx as nx


def intersections_dict(streets):
    G = nx.DiGraph()
    for street in streets.element():
        start = street['start_intersection']
        end = street['end_intersection']
        length = street['cross_time']
        G.add_edge(start, end, weight=length)

    return G.nodes()


def check_validity_T(streets, solution_T):

    intersections = intersections_dict(streets)
    validity = True
    intersection_key = 0
    while validity:

        intersection = intersections[intersection_key]
        number_of_green_lights = 0
        for street in intersection:
            light = solution_T[street]
            number_of_green_lights += light

        if number_of_green_lights > 1:
            validity = False

        intersection_key += 1

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
