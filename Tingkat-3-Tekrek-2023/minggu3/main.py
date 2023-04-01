graph = {
    'A': ['Z', 'S', 'T'],
    'Z': ['O'],
    'O': ['S1'],
    'S1': ['F', 'R'],
    'f': ['B'],
    'B': [],
    'R': [],
    'S': ['O1', 'F1', 'R1'],
    'O1': [],
    'F1': ['B1'],
    'B1': [],
    'R1': ['C', 'P'],
    'C': [],
    'P': [],
    'T': ['L'],
    'L': ['M'],
    'M': ['D'],
    'D': []
}

visited = set()  # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Depth First Search")

dfs(visited, graph, 'A')