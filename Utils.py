import csv
import random
import math
from math import pi

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def write_test_results(results):
    """
    appends test results to .csv file
    :param results: list of test results
    :return: None
    """
    with open(f'test_results.csv', "a") as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(results)
    return

def create_point(low,high):
    """
    Randomly generate values to create Point object
    :param low: lowest possible value
    :param high: highest possible value
    :return: Point object
    """
    range = high-low
    return Point(low+random.random()*range,low+random.random()*range)

def print_pretty(list):
    """
    :param list: list of points to print
    :return: None
    """
    for point in list:
        print(f"({point.x},{point.y})")

def polar_angle(p1, p2):
    y = p1.y - p2.y
    x = p1.x - p2.x
    ret = math.degrees(math.atan2(y,x))
    return ret

def distance(origin,p):
    """
    :return: distance between point origin and point p
    """
    AC = abs(origin.x - p.x)
    BC = abs(origin.y - p.y)
    AB = math.sqrt(pow(AC,2) + pow(BC,2))
    return AB

def is_left_turn(hull, p1, p2):
    """
    :return: True if p2 is left of line segment (hull,p1)
    """
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

def make_random_list(length):
    """
    creates a list of points with a random distribution
    :param length: length of desired list
    :return: generated list
   """
    list = []
    for i in range(0,length):
        list.append(create_point(0, 800))

    return list

def make_maxhull_list(length, center=(0,0), radius=500):
    """
    creates a list of points with min points on the hull
    and all other points within the hull.
    Math formula based on gist.github.com/danleyb2/ce6d2b82b1556f7bb7dc3c5d2bccb2fc
    :param length: length of desired list
    :return: generated list
    """
    center_x, center_y = center
    list = []
    for i in range(0,length):
        x = center_x + math.cos(2*pi/length*i)*radius
        y = center_y + math.sin(2*pi/length*i)*radius
        list.append(Point(x,y))
    return list

def make_minhull_list(length, center=(0,0),height=500):
    """
    My hacky way in create a triangle with points within in
    :param length: size of list to create
    :param center: center coordinate to build right angle
    :param height: height of triangle to create
    :return:
    """
    center_x, center_y = center
    a = Point(center_x, center_y)
    b = Point(center_x, center_y + height)
    c = Point(center_y + height, center_x)
    list = [a,b,c]
    for i in range(0,length):
        p = create_point(center_x+1, center_y+height-1)
        while(polar_angle(c, b) >= polar_angle(c, p)):
            p = create_point(center_x+1, center_y+height-1)
        list.append(p)
    return list

