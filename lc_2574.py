class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n

        left,right=[0]*n,[0]*n

        lsum,rsum=0,0
        i,j=1,n-2

        while i<n:
            lsum+=nums[i-1]
            left[i]=lsum
            i+=1
        
        while j>=0:
            rsum+=nums[j+1]
            right[j]=rsum
            j-=1
        
        for k in range(n):
            ans[k]=abs(left[k]-right[k])
        
        return ans
        
