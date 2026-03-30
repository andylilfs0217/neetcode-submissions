class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0

        n, m = len(grid), len(grid[0])
        visited = grid
        for j in range(m):
            for i in range(n):
                cell = visited[i][j]
                if cell == '1':
                    q = deque()
                    q.append((i, j))
                    while q:
                        y, x = q.popleft()
                        visited[y][x] = 0
                        if y - 1 >= 0 and visited[y-1][x] == '1':
                            q.append((y-1, x))
                        if x - 1 >= 0 and visited[y][x-1] == '1':
                            q.append((y, x-1))
                        if y + 1 < n and visited[y+1][x] == '1':
                            q.append((y+1, x))
                        if x + 1 < m and visited[y][x+1] == '1':
                            q.append((y, x+1))
                    ans += 1

        return ans