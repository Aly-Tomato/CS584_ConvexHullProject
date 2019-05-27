import csv
import math

class Point:
    def __init__(self, x, y, colour=None):
        self.x = x
        self.y = y
        if color is None:
            self.colour = color(0,0,0)
        else:
            self.colour = colour
                    
def write_csv(list):
    with open('test.txt', mode='w') as file:
        writer = csv.writer(file, delimiter=',')
        for blob in list:
            writer.writerow([blob.x, blob.y])
            
def create_point():
    return Point(random(width/8,width-width/8),random(height/8,height-height/8))


def print_pretty(list):
    """
    Method to help in debugging
    """
    for point in list:
        print("(" + str(point.x)+ ", " + str(point.y) + ")")


def polar_angle(p1, p2):
    y = p2.y - p1.y
    x = p2.x - p1.x
    ret = math.degrees(math.atan2(y,x))
    return ret

def distance(origin,p):
    AC = abs(origin.x - p.x)
    BC = abs(origin.y - p.y)
    AB = math.sqrt(pow(AC,2) + pow(BC,2))
    return AB

def is_left_turn(hull, p1, p2):
    m = ((p2.y-hull.y) * (p1.x - hull.x))
    n = ((p1.y - hull.y) * (p2.x - hull.x))
    if(m == n):
        # if points are collinear select furthest point
        if distance(hull, p1) >= distance(hull,p2):
            return True
        else:
            return False
    if(m < n):
        return True
    else:
        return False

def get_lowest_point(point_list):
    """
    :param list: of points
    :return: lowest point on the coordinate system
             furthest left if there is a tie
    """
    lowest_p = point_list[0]
    for p in point_list:
        if p.y < lowest_p.y:
            lowest_p = p
        if p.y == lowest_p.y:
            if p.x < lowest_p.x:
                lowest_p = p
    return lowest_p
