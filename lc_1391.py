class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        direct = {1: [(0,-1),(0,1)],2:[(-1,0),(1,0)],3:[(0,-1),(1,0)],4:[(0,1),(1,0)],5:[(0,-1),(-1,0)],6:[(-1,0),(0,1)]}

        m,n=len(grid),len(grid[0])

        def dfs(grid,i,j,vis):
            if i<0 or i>=m or j<0 or j>=n:
                return False
            if i==m-1 and j==n-1:
                return True
            
            if (i,j) in vis:
                return False
            
            vis.add((i,j))
            for di,dj in direct[grid[i][j]]:
                ni,nj=i+di,j+dj
                if ni<0 or ni>=m or nj<0 or nj>=n:
                    continue
                if (-di,-dj) in direct[grid[ni][nj]]:
                    if dfs(grid,ni,nj,vis):
                        return True
            
            return False
        
        return dfs(grid,0,0,set())
                
