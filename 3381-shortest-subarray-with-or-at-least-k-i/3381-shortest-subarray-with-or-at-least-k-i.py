class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = float("inf")
        l = 0
        r = 0
        temp = 0
        for i in nums:
            if(i>=k):
                return 1
        while(r<n):
            temp  = 0
            for i in range(l,r+1):
                temp = temp|nums[i]
            if(temp > k):
                ans = min(ans,r-l+1)
                l += 1
            elif(temp == k):
                ans = min(ans,r-l+1)
                l += 1
            else:
                r += 1
        return ans if(ans!=float("inf")) else -1