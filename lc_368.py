class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        
        nums.sort()
        n=len(nums)
        dp=[1]*n
        prev=[-1]*n
        maxL=1
        maxI=0

        i=0
        while i<n:
            j=0
            while j<i:

                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
                j+=1

            if dp[i]>maxL:
                maxL=dp[i]
                maxI=i
            
            i+=1
        # maxI=dp.index(max(dp))
        result=[]

        while maxI!=-1:
            result.append(nums[maxI])
            maxI=prev[maxI]
        
        return result[::-1]
        
                    

        
