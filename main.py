import turtle
import reeds_shepp as rs
import utils
import draw
import math
import networkx as nx
from networkx.algorithms.approximation import traveling_salesman_problem

def tsp_path(points):
    G = nx.Graph()
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = math.sqrt((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)
            G.add_edge(i, j, weight=dist)
    tsp_order = traveling_salesman_problem(G)
    return [points[i] for i in tsp_order]

def main(turn_radius):
    # points to be followed
    pts = [(-6, -7), (-6, 0), (-4, 6), (0, 5), (0, -2), (-2, -6), (3, -5), (3, 6), (6, 4)]

    # Solve TSP to get optimal order of points
    ordered_pts = tsp_path(pts)
    print("Ordered Points: ", ordered_pts)

    # generate PATH so the vectors are pointing at each other
    PATH = []
    for i in range(len(ordered_pts) - 1):
        dx = ordered_pts[i + 1][0] - ordered_pts[i][0]
        dy = ordered_pts[i + 1][1] - ordered_pts[i][1]
        theta = math.atan2(dy, dx)
        PATH.append((ordered_pts[i][0], ordered_pts[i][1], utils.rad2deg(theta)))
    PATH.append((ordered_pts[-1][0], ordered_pts[-1][1], 0))

    # init turtle
    tesla = turtle.Turtle()
    tesla.speed(0)  # 0: fast; 1: slow, 8.4: cool
    tesla.shape('arrow')
    tesla.resizemode('user')
    tesla.shapesize(1, 1)

    # draw vectors representing points in PATH
    for pt in PATH:
        draw.goto(tesla, pt)
        draw.vec(tesla)

    # draw all routes found
    tesla.speed(0)
    for i in range(len(PATH) - 1):
        paths = rs.get_all_paths(PATH[i], PATH[i + 1], turn_radius)
        for path in paths:
            draw.set_random_pencolor(tesla)
            draw.goto(tesla, PATH[i])
            draw.draw_path(tesla, path)

    # draw shortest route
    tesla.pencolor(1, 0, 0)
    tesla.pensize(3)
    tesla.speed(10)
    draw.goto(tesla, PATH[0])
    path_length = 0
    for i in range(len(PATH) - 1):
        path = rs.get_optimal_path(PATH[i], PATH[i + 1], turn_radius)
        path_length += rs.path_length(path)
        draw.draw_path(tesla, path)

    print("Shortest path length: {} px.".format(int(draw.scale(path_length))))

    turtle.done()

def main2(turn_radius):
    # points to be followed
    pts = [(14, -7), (14, 0), (16, 6), (20, 5), (20, -2), (18, -6), (23, -5), (23, 6), (26, 4)]

    # Solve TSP to get optimal order of points
    ordered_pts = tsp_path(pts)
    print("Ordered Points: ", ordered_pts)

    # generate PATH so the vectors are pointing at each other
    PATH = []
    for i in range(len(ordered_pts) - 1):
        dx = ordered_pts[i + 1][0] - ordered_pts[i][0]
        dy = ordered_pts[i + 1][1] - ordered_pts[i][1]
        theta = math.atan2(dy, dx)
        PATH.append((ordered_pts[i][0], ordered_pts[i][1], utils.rad2deg(theta)))
    PATH.append((ordered_pts[-1][0], ordered_pts[-1][1], 0))

    # init turtle
    tesla = turtle.Turtle()
    tesla.speed(0)  # 0: fast; 1: slow, 8.4: cool
    tesla.shape('arrow')
    tesla.resizemode('user')
    tesla.shapesize(1, 1)

    # draw vectors representing points in PATH
    for pt in PATH:
        draw.goto(tesla, pt)
        draw.vec(tesla)

    # draw all routes found
    tesla.speed(0)
    for i in range(len(PATH) - 1):
        paths = rs.get_all_paths(PATH[i], PATH[i + 1], turn_radius)
        for path in paths:
            draw.set_random_pencolor(tesla)
            draw.goto(tesla, PATH[i])
            draw.draw_path(tesla, path)

    # draw shortest route
    tesla.pencolor(1, 0, 0)
    tesla.pensize(3)
    tesla.speed(10)
    draw.goto(tesla, PATH[0])
    path_length = 0
    for i in range(len(PATH) - 1):
        path = rs.get_optimal_path(PATH[i], PATH[i + 1], turn_radius)
        path_length += rs.path_length(path)
        draw.draw_path(tesla, path)

    print("Shortest path length: {} px.".format(int(draw.scale(path_length))))

    turtle.done()


if __name__ == '__main__':
    turn_radius = 5.0  # Set initial turn radius
    #turn_radius2 = 5.0  # Set initial turn radius
    main(turn_radius)
    #main2(turn_radius2)
