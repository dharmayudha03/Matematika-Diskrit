class Simpul:
    def __init__(self):
        self.Left = None
        self.INFO = 0
        self.Right = None

def shortest_path(A, start, dest):
    dist = [float('inf')] * 9
    visited = [False] * 9
    parent = [-1] * 9

    dist[start] = 0

    for _ in range(9):
        min_dist = float('inf')
        min_index = -1

        for j in range(9):
            if not visited[j] and dist[j] < min_dist:
                min_dist = dist[j]
                min_index = j

        if min_index == -1:
            break

        visited[min_index] = True

        for j in range(9):
            if A[min_index][j] != 0 and not visited[j]:
                alt_dist = dist[min_index] + A[min_index][j]
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

def longest_path(A, start, dest):
    dist = [float('-inf')] * 9
    visited = [False] * 9
    parent = [-1] * 9

    dist[start] = 0

    for _ in range(9):
        max_dist = float('-inf')
        max_index = -1

        for j in range(9):
            if not visited[j] and dist[j] > max_dist:
                max_dist = dist[j]
                max_index = j

        if max_index == -1:
            break

        visited[max_index] = True

        for j in range(9):
            if A[max_index][j] != 0 and not visited[j]:
                alt_dist = dist[max_index] + A[max_index][j]
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

def PrintPath(path, A, cost):
    result = ""
    for i in range(len(path)):
        result += chr(path[i] + ord('A'))
        if i != len(path) - 1:
            result += f" ({A[path[i]][path[i + 1]]}) -> "
    result += f"\nTotal Jarak: {cost}"
    return result

A = [
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

PointS = [None] * 9
FIRST = Simpul()
P = FIRST
P.Left = None
P.Right = None
P.INFO = 0
PointS[0] = P
Q = P  # Perbaikan disini, memastikan Q tidak None
print(f"{chr(P.INFO + ord('A'))} alamat = {hex(id(PointS[0]))}")

for i in range(1, 9):
    P = Simpul()
    P.Left = None
    P.Right = None
    P.INFO = i
    PointS[i] = P
    Q.Left = P  # Perbaikan disini, menghubungkan Q dengan P
    Q = P  # Perbaikan disini, meng-update Q
    print(f"{chr(P.INFO + ord('A'))} alamat = {hex(id(PointS[i]))}")

Q = FIRST
for i in range(9):
    R = Q
    print(f"\nVertex {chr(Q.INFO + ord('A'))}", end="")
    for j in range(9):
        if A[i][j] != 0:
            P = Simpul()
            P.INFO = A[i][j]
            R.Right = P
            P.Left = PointS[j]
            print(f" berhubungan dengan {chr(P.Left.INFO + ord('A'))},", end="")
            print(f" dengan bobot = {P.INFO}. ", end="")
            P.Right = None
            R = P
    Q = Q.Left

print()

shortest_path_result = shortest_path(A, 0, 8)
longest_path_result = longest_path(A, 0, 8)

print(f"\nJarak Terpendek Dari A ke I: {PrintPath(shortest_path_result[0], A, shortest_path_result[1])}")
print(f"Jarak Terpanjang Dari A ke I: {PrintPath(longest_path_result[0], A, longest_path_result[1])}")
