class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if(n==1 or n == 0):
            return 0
        nums = sorted(nums, reverse = True)
        mini_diff = max(nums)-min(nums)
        for i in range(n-k+1):
            mini_diff = min(mini_diff, nums[i]-nums[i+k-1])
        return mini_diff
