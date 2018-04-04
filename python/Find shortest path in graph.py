def find_all_paths(graph, start, end, path=None):
    if start not in graph:
        return []

    if path is None:
        path = []
    path = path + [start]

    if start == end:
        return [path]

    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


dept = 'A'
dest = 'E'
inputs = [
    'A B 3',
    'A C 10',
    'B D 2',
    'B E 5',
    'C E 1',
    'D E 4',
]

segs = []
for s in inputs:
    l = s.split()
    segs.append((l[0], l[1], int(l[2])))

graph = {}
for seg in segs:
    if seg[0] in graph:
        graph[seg[0]][seg[1]] = seg[2]
    else:
        graph[seg[0]] = {seg[1]: seg[2]}

    if seg[1] in graph:
        graph[seg[1]][seg[0]] = seg[2]
    else:
        graph[seg[1]] = {seg[0]: seg[2]}

paths = find_all_paths(graph, dept, dest)
dists = []
for path in paths:
    dist = 0
    for i, node in enumerate(path[:-1]):
        dist += graph[node][path[i+1]]
    dists.append(dist)

paths = sorted(list(zip(dists, paths)), key=lambda t: t[0])

for path in paths:
    print(path)
