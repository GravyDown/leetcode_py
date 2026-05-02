class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        t=[[-1 for _ in range(101)]for _ in range(101)]
        def solve(m,n,i,j):
            if i>=m or j>=n:
                return 0
            
            if i==m-1 and j==n-1:
                return 1
            
            if t[i][j]!=-1:
                return t[i][j]
            else:
                t[i][j] = solve(m,n,i,j+1) + solve(m,n,i+1,j)
                return solve(m,n,i,j+1) + solve(m,n,i+1,j)
        
        return solve(m,n,0,0)
