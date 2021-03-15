'''
음료수 얼려 먹기
N * M에 구명이 뚫린 부분은 0, 칸막이가 존재하는 부분은 1로 표시된 얼음틀이 있다.
얼음 틀 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성.
'''
from collections import deque

'''
python 자료형은 크게 mutable, immutable (불변)으로 나뉘는데,
불변 타입 (int, str)의 객체를 넘기면 call by value
가변 타입 (list, dict)의 객체를 넘기면 call by reference.
'''


def bfs(i, j, mold):
    q = deque([(i, j)])
    mold[i][j] = -1

    while q:
        x, y = q.popleft()

        for dx, dy in pos:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
            if mold[nx][ny] ** 2 == 1: continue

            q.append((nx, ny))
            mold[nx][ny] = -1


pos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

n, m = map(int, input().split())
mold = []

for _ in range(n):
    mold.append(list(map(int, input())))

count = 0
for i in range(n):
    for j in range(m):
        if mold[i][j] == 0:
            bfs(i, j, mold)
            count += 1
print(count)
