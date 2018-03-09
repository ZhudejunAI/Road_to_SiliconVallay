from __future__ import print_function
import numpy as np


def fill_graph(graph, new_color, x, y):
    m = len(graph)
    n = len(graph[0])

    old_color = graph[x][y]
    if old_color == new_color:
        return

    graph[x][y] = new_color

    if x > 0 and graph[x - 1][y] == old_color:
        fill_graph(graph, new_color, x - 1, y)

    if x < m - 1 and graph[x + 1][y] == old_color:
        fill_graph(graph, new_color, x + 1, y)

    if y > 0 and graph[x][y - 1] == old_color:
        fill_graph(graph, new_color, x, y - 1)

    if y < n - 1 and graph[x][y + 1] == old_color:
        fill_graph(graph, new_color, x, y + 1)


def main():
    image = [[1, 1, 3, 4, 4, 4],
             [1, 3, 3, 3, 2, 4],
             [2, 2, 3, 3, 2, 2],
             [4, 4, 3, 2, 2, 4],
             [2, 2, 2, 2, 4, 4]]

    fill_graph(image, 5, 2, 4)

    for color in image:
        print(color)


if __name__ == '__main__':
    main()
