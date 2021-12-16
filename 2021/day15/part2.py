from copy import deepcopy
from queue import PriorityQueue


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


def get_neighbors(matrix, node):
    j, i = node[0], node[1]

    neighbors = []
    if j - 1 >= 0 and (j - 1, i):
        neighbors.append(matrix[j - 1][i])
    if j + 1 < len(matrix):
        neighbors.append(matrix[j + 1][i])
    if i - 1 >= 0 and (j, i - 1):
        neighbors.append(matrix[j][i - 1])
    if i + 1 < len(matrix):
        neighbors.append(matrix[j][i + 1])

    return []


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
    visited = []

    res = {v: float("inf") for v in range(len(matrix))}
    res[0] = 0
    pq = PriorityQueue()
    pq.put((0, (0, 0)))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        visited.append(current_vertex)

        for neighbor in get_neighbors(matrix, current_vertex):
            pass
            # if matrix[current_vertex][neighbor] != -1:
            #     distance = matrix[current_vertex][neighbor]
            #     if neighbor not in visited:
            #         old_cost = D[neighbor]
            #         new_cost = D[current_vertex] + distance
            #         if new_cost < old_cost:
            #             pq.put((new_cost, neighbor))
            #             D[neighbor] = new_cost
    for vertex in range(len(res)):
        print("Distance from vertex 0 to vertex", vertex, "is", res[vertex])


if __name__ == "__main__":
    main()