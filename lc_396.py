class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        def helper(arr):
            ret=0
            for i in range(len(arr)):
                ret += arr[i]*i 
            return ret

        n=len(nums)
        s=sum(nums)
        res=helper(nums)
        f=res

        for i in range(1,n):
            f=f+s - n*nums[n-i]
            res = max(res,f)

        return res
