import Utils

def do_Jarvis(point_list):
    """
    Jarvis March method to solve Convex Hull
    :param point_list: set of Utils.Points
    :return: hull_list: list of Utils.Points on hull
    """
    hull_list = [Utils.get_lowest_point(point_list)]

    for hull_point in hull_list:
        next_point = point_list[0]
        for p in point_list:
            if Utils.is_left_turn(hull_point, p, next_point):
                next_point = p
        if next_point != hull_list[0]:
            hull_list.append(next_point)
    return hull_list
