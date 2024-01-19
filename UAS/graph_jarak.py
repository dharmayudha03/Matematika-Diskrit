class Node:
    def __init__(self, info=None):
        self.info = info
        self.left = None
        self.right = None



def shortest_path(matrix, start, dest):
    dist = [float('inf')] * len(matrix)
    visited = [False] * len(matrix)
    parent = [-1] * len(matrix)

    dist[start] = 0

    for _ in range(len(matrix)):
        min_dist = float('inf')
        min_index = -1

        for j in range(len(matrix)):
            if not visited[j] and dist[j] < min_dist:
                min_dist = dist[j]
                min_index = j

        if min_index == -1:
            break

        visited[min_index] = True

        for j in range(len(matrix)):
            if matrix[min_index][j] != 0 and not visited[j]:
                alt_dist = dist[min_index] + matrix[min_index][j]
                if alt_dist < dist[j]:
                    dist[j] = alt_dist
                    parent[j] = min_index

    path = []
    v = dest
    while v != -1:
        path.append(v)
        v = parent[v]
    path.reverse()

    return path, dist[dest]


def longest_path(matrix, start, dest):
    dist = [float('-inf')] * len(matrix)
    visited = [False] * len(matrix)
    parent = [-1] * len(matrix)

    dist[start] = 0

    for _ in range(len(matrix)):
        max_dist = float('-inf')
        max_index = -1

        for j in range(len(matrix)):
            if not visited[j] and dist[j] > max_dist:
                max_dist = dist[j]
                max_index = j

        if max_index == -1:
            break

        visited[max_index] = True

        for j in range(len(matrix)):
            if matrix[max_index][j] != 0 and not visited[j]:
                alt_dist = dist[max_index] + matrix[max_index][j]
                if alt_dist > dist[j]:
                    dist[j] = alt_dist
                    parent[j] = max_index

    path = []
    v = dest
    while v != -1:
        path.append(v)
        v = parent[v]
    path.reverse()

    return path, dist[dest]


def print_path(path, matrix, cost):
    result = ""
    for i in range(len(path)):
        result += chr(path[i] + ord('A'))
        if i != len(path) - 1:
            result += f" ({matrix[path[i]][path[i + 1]]}) -> "
    result += f"\nTotal Jarak: {cost}"
    return result


matrix1 = [
    [0, 5, 3, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 3, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 4, 0, 0],
    [0, 4, 5, 0, 5, 6, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 5, 0],
    [0, 0, 3, 0, 0, 0, 6, 0, 8],
    [0, 0, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 0, 0, 4, 6, 0, 0, 7],
    [0, 0, 0, 0, 0, 0, 9, 0, 0]
]

points = [None] * len(matrix1)
first = Node(0)
current = first
current.left = None
current.right = None
current.info = 0
points[0] = current
q = current

print(f"{chr(current.info + ord('A'))} alamat = {hex(id(points[0]))}")

for i in range(1, len(matrix1)):
    current = Node()
    current.left = None
    current.right = None
    current.info = i
    points[i] = current
    q.left = current
    q = current
    print(f"{chr(current.info + ord('A'))} alamat = {hex(id(points[i]))}")

q = first
for i in range(len(matrix1)):
    r = q
    print(f"\nVertex {chr(q.info + ord('A'))}", end="")
    for j in range(len(matrix1)):
        if matrix1[i][j] != 0:
            current = Node()
            current.info = matrix1[i][j]
            r.right = current
            current.left = points[j]
            print(f" berhubungan dengan {chr(current.left.info + ord('A'))},", end="")
            print(f" dengan bobot = {current.info}. ", end="")
            current.right = None
            r = current
    q = q.left

print()

shortest_path_result = shortest_path(matrix1, 0, 8)
longest_path_result = longest_path(matrix1, 0, 8)

print(f"\nJarak Terpendek Dari A ke I: {print_path(shortest_path_result[0], matrix1, shortest_path_result[1])}")
print(f"Jarak Terpanjang Dari A ke I: {print_path(longest_path_result[0], matrix1, longest_path_result[1])}")
