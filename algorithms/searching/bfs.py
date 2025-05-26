graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E', 'F'],
    'C': ['A', 'G'],
    'D': [],
    'E': [],
    'F': ['H'],
    'G': ['I'],
    'H': [],
    'I': [],
}

# Time Complexity - O(|V| + |E|)
def bfs(graph, node):
    visited = []
    queue = []

    visited.append(node)
    queue.append(node)

    while queue:
        q = queue.pop(0)
        print(q, end = " ")

        for n in graph[q]:
            if n not in visited:
                visited.append(n)
                queue.append(n)

def test():
    print(bfs(graph, 'B'))

if __name__ == "__main__":
  test()
