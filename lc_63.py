class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        t=[[-1 for _ in range(101)]for _ in range(101)]

        def solve(grid,i,j):
            if i>=m or j>=n:
                return 0
            
            if grid[i][j]==1:
                return 0
            
            if i==m-1 and j==n-1:
                return 1
            
            if t[i][j]!=-1:
                return t[i][j]
            else:
                t[i][j] = solve(grid,i,j+1) + solve(grid,i+1,j)
                return t[i][j]
        
        return solve(obstacleGrid,0,0)
