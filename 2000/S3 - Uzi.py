# Take inputs

N = int(input())

g = {}

import re

def gengraph(graph, pagenum):
    imp = ""
    for e in range(76):
        z = ""
        for f in range(e):
            z+="."
        z += "|"
        imp += z
        
    for _ in range(pagenum):
        temp = []
        key = input()
        l = ""
        # Add page
        while l != "</HTML>":
            l = input()
            temp.append(l)

        links = []
        
        # Look for links in page
        for line in temp:
            m = re.findall("http({0})>".format(imp), line)
            if len(m) > 0:
                for o in range(0, len(m)):
                    
                    link = "http" + m[o][:-1]
                    links.append(link)

        # Add key:value to graph
        graph[key] = links

from queue import Queue

def iter_BFS(graph, start, target):
    # Perform BFS and print the appropriate output strings for each
    visited = set()
    queue = Queue()

    queue.put(start)
    visited.add(start)
    parent = dict()
    parent[start] = None

    path_found = False
    while not queue.empty():
        current_node = queue.get()
        if current_node == target:
            path_found = True
            break

        for next_node in graph[current_node]:
            if next_node not in visited:
                queue.put(next_node)
                parent[next_node] = current_node
                visited.add(next_node)

    if path_found:
        print("Can surf from {0} to {1}".format(start, target))
    else:
        print("Can't surf from {0} to {1}".format(start, target))


gengraph(g, N)

# Get pairs of values to search for
t = ""
vals = []
temp = []
count = 0
while t != "The End":
    t = input()
    count += 1
    temp.append(t)
    if count % 2 == 0:
        vals.append(temp)
        temp = []

# Output graph edges
for x in g:
    for y in g[x]:
        print("Link from {0} to {1}".format(x, y))

print()

for v in vals:
    iter_BFS(g, v[0], v[1])

    
