def solve(instance):
    D = instance['headers']['duration']
    streets = instance['streets']
    nb_streets = len(streets)
    print(f'nb_streets: {nb_streets}')
    intersection_with_green_light = [False] * D 
    res = [str(D)]
    for i in range(1, D+1):
        is_attributed = False
        nb_street = 0
        while not is_attributed:
            street = streets[nb_street]
            if street['end_intersection'] == i and intersection_with_green_light[i] == False:
                intersection_with_green_light[i] = True
                res.append('i')
                res.append('1')
                res.append(street['name']+' '+str(D))
                is_attributed = True
            elif nb_street == streets-1:
                is_attributed = True
            else:
                nb_street += 1
    return  "\n".join(str(i) for i in res)
