class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid[0]) == 0:
            return 0

        R, C = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                d = [[1,0], [-1,0], [0,1], [0,-1]]

                for dr, dc in d:
                    r, c = row + dr, col + dc

                    if(
                        r in range(R) and c in range(C)
                        and grid[r][c] == "1" and (r,c) not in visit
                    ):
                        q.append((r,c))
                        visit.add((r,c))

        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1" and (i,j) not in visit:
                    bfs(i, j)
                    islands += 1
        return islands