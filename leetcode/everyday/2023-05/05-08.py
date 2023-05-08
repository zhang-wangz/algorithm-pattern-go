from collections import deque
from itertools import pairwise
from typing import List

# 0-1bfs
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def f(i, j):
            return i * n + j
        def check(i, j):
            return 0<=i<m and 0<=j<n and grid[i][j] != '#'
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == 'S':
                    si, sj = i, j
                elif c == 'B':
                    bi, bj = i, j
        q = deque([(f(si, sj), f(bi, bj), 0)])
        vis = [[False] * (m*n) for _ in range(m*n)]
        vis[f(si, sj)][f(bi, bj)] = True
        dirs = [-1, 0, 1, 0, -1]
        while q:
            s, b, d = q.popleft()
            bi, bj = b // n, b % n
            if grid[bi][bj] == 'T':
                return d
            si, sj = s // n, s % n
            for a, b in pairwise(dirs):
                sx, sy = si + a, sj + b
                if not check(sx, sy):
                    continue
                if sx == bi and sy == bj:
                    bx, by = bi+a, bj+b
                    if not check(bx, by) or vis[f(sx, sy)][f(bx, by)]:
                        continue
                    vis[f(sx, sy)][f(bx, by)] = True
                    q.append((f(sx,sy), f(bx, by), d+1))
                elif not vis[f(sx, sy)][f(bi, bj)]:
                    vis[f(sx, sy)][f(bi, bj)] = True
                    q.appendleft((f(sx,sy), f(bi, bj), d))
        return -1