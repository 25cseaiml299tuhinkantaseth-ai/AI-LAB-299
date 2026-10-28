from collections import deque
def bfs_traversal(graph, start_node):
    visited = set()
    queue = deque()
    visited.add(start_node)
    queue.append(start_node)
    print("BFS Traversal Order:", end=" ")
    while queue:
        current = queue.popleft()
        print(current, end=" ")
        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
# Example graph
ex_graph = {
    'K': ['L', 'P'], 'L': ['N'], 'P': ['M'], 'N': ['O'], 'M': [], 'O': []
}
bfs_traversal(ex_graph, 'K')