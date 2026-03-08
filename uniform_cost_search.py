import heapq

def uniform_cost_search(graph, start, goal):
    visited = set()
    queue = [(0, start, [start])]  # (cost, node, path)

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return cost, path

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path + [neighbor]))

    return None


# Taking graph input from user
graph = {}
n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node: ")
    neighbors = []
    m = int(input("Enter number of neighbors: "))

    for j in range(m):
        neighbor = input("Enter neighbor node: ")
        cost = int(input("Enter cost: "))
        neighbors.append((neighbor, cost))

    graph[node] = neighbors

start = input("Enter start node: ")
goal = input("Enter goal node: ")

result = uniform_cost_search(graph, start, goal)

if result:
    cost, path = result
    print("\nOptimal Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found")
