class Solution:
    def checkBoundary(self, i, j, n, m) -> bool:
        return i >= 0 and i < n and j >= 0 and j < m
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]
        max_area = 0

        n, m = len(grid), len(grid[0])
        visited_grid = grid
        for i in range(n):
            for j in range(m):
                cell = visited_grid[i][j]
                if cell == 1:
                    q = deque()
                    q.append((i, j))
                    visited_grid[i][j] = 0
                    area = 0
                    while q:
                        area += 1
                        y, x = q.popleft()
                        for dy, dx in directions:
                            ny, nx = y + dy, x + dx
                            is_safe = self.checkBoundary(ny, nx, n, m)
                            if is_safe and visited_grid[ny][nx] == 1:
                                q.append((ny, nx))
                                visited_grid[ny][nx] = 0
                    max_area = max(max_area, area)

        return max_area