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


def get_neighbors(matrix, node, visited):
    j, i = node[0], node[1]

    neighbors = []
    if j - 1 >= 0 and (j - 1, i) not in visited:
        neighbors.append((j - 1, i))
    if j + 1 < len(matrix) and (j + 1, i) not in visited:
        neighbors.append((j + 1, i))
    if i - 1 >= 0 and (j, i - 1) not in visited:
        neighbors.append((j, i - 1))
    if i + 1 < len(matrix) and (j, i + 1) not in visited:
        neighbors.append((j, i + 1))

    return neighbors


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

    res = [[float("inf")] * len(matrix) for v in range(len(matrix))]
    res[0][0] = 0
    pq = PriorityQueue()
    pq.put((0, (0, 0)))
    counter = 0
    while not pq.empty():
        print(counter)
        (dist, cv) = pq.get()
        visited.add(cv)

        for neighbor in get_neighbors(matrix, cv, visited):
            x, y = neighbor[0], neighbor[1]
            distance = matrix[x][y]
            if neighbor not in visited:
                old_cost = res[x][y]
                new_cost = res[cv[0]][cv[1]] + distance
                if new_cost < old_cost:
                    pq.put((new_cost, neighbor))
                    res[x][y] = new_cost
        counter += 1

    print(res[-1][-1])


if __name__ == "__main__":
    main()