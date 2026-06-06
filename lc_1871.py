class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n=len(s)
        dp=[False]*n
        dp[0]=True
        pre=[0]*n
        pre[0]=1

        for j in range(1,n):
            if j-minJump>=0:
                if pre[j-minJump] - (pre[j-maxJump-1] if j-maxJump-1 >= 0 else 0) > 0 and s[j]=='0':
                    dp[j]=True
            pre[j]=pre[j-1]+int(dp[j])
        
        return dp[n-1]
