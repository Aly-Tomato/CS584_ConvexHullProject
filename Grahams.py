import Utils

def sort_polar(p0, point_list):
    graph = {}
    sorted_points = []
    for p in point_list:
        polar = Utils.polar_angle(p,p0)
        if polar in graph.keys():
            a = Utils.polar_angle(graph[polar], p0)
            b = Utils.polar_angle(p, p0)
            if a == b:
                if Utils.distance(p0,graph[polar]) < Utils.distance(p0, p):
                    graph[polar] = p
        else:
            graph[polar] = p
    sgraph = sorted(graph)
    for k in sgraph:
        sorted_points.append(graph[k])
    return sorted_points


def do_Grahams(point_list):
    """
    Graham Scan method to solve Convex Hull
    :param point_list: set of Utils.Points
    :return: hull_list: list of Utils.Points on hull
    """
    hull_stack = []
    lowest_p = Utils.get_lowest_point(point_list)
    hull_stack.append(lowest_p)
    sorted_points = sort_polar(lowest_p, point_list)
    for p in sorted_points:
        if p == lowest_p:
            continue
        counter = len(hull_stack)
        while counter > 1 and Utils.is_left_turn(hull_stack[counter-2], hull_stack[counter-1],p):
            hull_stack.pop()
            counter -= 1
        hull_stack.append(p)
    return hull_stack
