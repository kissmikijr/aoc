from collections import defaultdict

num_of_paths = 0


def find_path(node, graph, visited):
    global num_of_paths
    if node == 'end':
        num_of_paths += 1

    visited.add(node)
    for n in graph[node]:
        if n.isupper() or n not in visited:
            find_path(n, graph, visited)
    if node in visited:
        visited.remove(node)


def main():
    nodes = []
    graph = defaultdict(list)
    with open('input.txt') as nodes:
        for n in nodes.read().split("\n"):
            x, y = n.split("-")
            graph[x].append(y)
            graph[y].append(x)
    visited = set()
    visited.add('start')
    find_path('start', graph, visited)
    print(num_of_paths)


if __name__ == "__main__":
    main()