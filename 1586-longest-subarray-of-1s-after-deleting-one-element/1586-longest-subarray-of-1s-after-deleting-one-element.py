class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = 0
        maxi = float("-inf")
        # if(1 not in nums):
        #     return -1
        # elif(0 not in nums):
        #     return n-1
        count_zero = 0
        while(r<n):
            if(nums[r] == 0):
                count_zero += 1
            while(count_zero>1):
                if(nums[l] == 0):
                    count_zero -= 1
                l += 1
            maxi = max(maxi, r-l)
            r += 1
        return maxi