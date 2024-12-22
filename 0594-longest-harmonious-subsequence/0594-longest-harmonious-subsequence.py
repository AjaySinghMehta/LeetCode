class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)
        ans = 0
        l = 0
        r = 1
        temp = []
        while(r<n):
            if(nums[r] - nums[l] == 1):
                ans = max(ans , r-l+1)
                r += 1
            elif(nums[r]-nums[l] > 1):
                l += 1
            else:
                r += 1
        return ans