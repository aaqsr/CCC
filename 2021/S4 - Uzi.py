N, W, D = map(int, input().split())

G = {}

# Input Processing / Graph population

# Initialization
for s in range(1, N+1):
    G[s] = [0, 0] # Walkway, station

# Store Walkway info
for _ in range(W):
    key, val = map(int, input().split())
    G[key][0] = val

# Store station info
initial = list(map(int, input().split()))

for i in range(len(initial)):
    key = initial[i]
    if i+1 >= len(initial):
        val = 0 # Doesn't lead anywhere
    else:
        val = initial[i+1]
    G[key][1] = val

# Subroutines

def updategraph(graph, node1, node2):
    global N
    # Swap all children nodes
    
    # If neighbours
    if graph[node1][1] == node2:
        temp = graph[node2][1]
        graph[node2][1] = node1
        graph[node1][1] = temp
        
    elif graph[node2][1] == node1:
        temp = graph[node1][1]
        graph[node1][1] = node2
        graph[node2][1] = temp
    else:
        # General case
        temp = graph[node1][1]
        graph[node1][1] = graph[node2][1]
        graph[node2][1] = temp

    # Swap all references

    for i in range(1, N+1):
        if not(i == node1 or i == node2):
            if graph[i][1] == node1:
                graph[i][1] = node2
            elif graph[i][1] == node2:
                graph[i][1] = node1
    
from queue import Queue

def BFS(graph, k):
    global N

    start = 1
    target = N
    time = 0
    
    visited = set()
    queue = Queue()

    queue.put(start)
    visited.add(start)
    parent = dict()
    parent[start] = None

    path_found = False
    
    while not queue.empty() and not path_found:
        current_node = queue.get()
        time += 1
        if current_node == target:
            path_found = True
            break

        next_node = graph[current_node][k]
        
        if not next_node == 0:
            if next_node not in visited:
                queue.put(next_node)
                parent[next_node] = current_node
                visited.add(next_node)

    return time

# Driver Code

for _ in range(D):
    swap1, swap2 = map(int, input().split())
    updategraph(G, initial[swap1-1], initial[swap2-1])
    walking = BFS(G, 0)
    station = BFS(G, 1)

    if station > walking:
        print(walking)
    else:
        print(station)
    

