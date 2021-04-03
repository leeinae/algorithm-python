def find_parent(n):
    if parent[n] != n:
        parent[n] = find_parent(parent[n])
    return parent[n]


def union_find(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

flag = False
for i in range(1, v + 1):
    a, b = map(int, input().split())
    if find_parent(a) == find_parent(b):
        flag = True
        break
    else:
        union_find(a, b)

print(flag)
