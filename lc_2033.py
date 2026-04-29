class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m,n=len(grid),len(grid[0])

        v=grid[0][0]%x
        for i in range(m):
            for j in range(n):
                if grid[i][j]%x != v:
                    return -1
        
        arr = sorted([val for row in grid for val in row])
        median = arr[(m*n)//2]

        ops=0
        for i in range(m):
            for j in range(n):
                diff = abs(grid[i][j] - median)
                ops+=diff//x
        
        return ops
