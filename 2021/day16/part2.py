from copy import deepcopy


def bump_matrix(matrix):
    cm = deepcopy(matrix)
    for i in range(len(cm)):
        for j in range(len(cm[i])):
            cm[i][j] += 1
            if cm[i][j] == 10:
                cm[i][j] = 1
    return cm


def create_matrix_row(matrix, length):
    big_chungus_matrix_row = deepcopy(matrix)
    bumpped_matrix = deepcopy(matrix)
    for _ in range(length):
        a = bump_matrix(bumpped_matrix)
        for i in range(len(a)):
            for j in range(len(a[i])):
                big_chungus_matrix_row[i].append(a[i][j])
        bumpped_matrix = a
    return big_chungus_matrix_row


import numpy as np


def main():
    matrix = []
    with open('input.txt') as matrix:
        matrix = [[int(x) for x in list(y)] for y in matrix.read().split("\n")]

    first_row = create_matrix_row(matrix, 4)
    r = deepcopy(matrix)
    for i in range(4):
        r = bump_matrix(r)
        second = create_matrix_row(r, 4)
        for z in second:
            first_row.append(z)

    matrix = first_row
    visited = set()
    solution = {}
    unvisited = []
    for i, row in enumerate(matrix):
        for j, _ in enumerate(row):
            solution[(j, i)] = {
                "prev": None,
                "sd": float('inf'),
                "node": (j, i)
            }
            unvisited.append({
                "prev": None,
                "sd": float('inf'),
                "node": (j, i)
            })
    solution[(0, 0)]["sd"] = 0

    from queue import PriorityQueue
    pq = PriorityQueue()
    pq.put((0, (0, 0)))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        visited.add(current_vertex)


        for n in range(len(matrix)*len(matrix)):
            


        obj = min(solution.values(), key=lambda x: x["sd"])
        node = obj["node"]
        prev_dist = obj["sd"]
        j, i = node[0], node[1]

        if j - 1 >= 0 and (j - 1, i) not in visited:
            up = matrix[j - 1][i]
            solution[(j - 1, i)]["sd"] = min(solution[(j - 1), i]["sd"],
                                             prev_dist + up)
            solution[(j - 1), i]["prev"] = node
        if j + 1 < len(matrix) and (j + 1, i) not in visited:
            down = matrix[j + 1][i]
            solution[(j + 1, i)]["sd"] = min(solution[(j + 1, i)]["sd"],
                                             prev_dist + down)
            solution[(j + 1, i)]["prev"] = node
        if i - 1 >= 0 and (j, i - 1) not in visited:
            left = matrix[j][i - 1]
            known_distance = solution[(j, i - 1)]["sd"]
            solution[(j, i - 1)]["sd"] = min(known_distance, prev_dist + left)
            solution[(j, i - 1)]["prev"] = node
        if i + 1 < len(matrix) and (j, i + 1) not in visited:
            right = matrix[j][i + 1]
            known_distance = solution[(j, i + 1)]["sd"]
            solution[(j, i + 1)]["sd"] = min(known_distance, prev_dist + right)
            solution[(j, i + 1)]["prev"] = node

        visited.add(node)

    print(solution[(len(matrix) - 1, len(matrix) - 1)])

    # if i == 0 and j == 0:
    #     continue
    # elif j - 1 < 0:
    #     matrix[i][j] += matrix[i - 1][j]
    # elif i - 1 < 0:
    #     matrix[i][j] += matrix[i][j - 1]
    # else:
    #     matrix[i][j] += min(matrix[i][j - 1], matrix[i - 1][j], )

    # for r in matrix:
    #     print(r)
    print(matrix[-1][-1] - matrix[0][0])


if __name__ == "__main__":
    main()