from collections import defaultdict

num_of_paths = 0


def find_path(node, graph, visited, visited_twice):
    global num_of_paths
    if node == 'end':
        num_of_paths += 1
        return

    visited[node] += 1
    for n in graph[node]:
        if n.isupper() or visited[n] == 0:
            find_path(n, graph, visited, visited_twice)
        elif visited[n] == 1 and not visited_twice:
            find_path(n, graph, visited, True)
    visited[node] -= 1


def main():
    nodes = []
    graph = defaultdict(list)
    with open('input.txt') as nodes:
        for n in nodes.read().split("\n"):
            x, y = n.split("-")
            graph[x].append(y)
            graph[y].append(x)
    print(graph)
    visited = defaultdict(int)
    visited['start'] += 2
    find_path('start', graph, visited, False)
    print(num_of_paths)


if __name__ == "__main__":
    main()