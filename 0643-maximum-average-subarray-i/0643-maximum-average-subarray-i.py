import statistics
class Solution:
    
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if(n == 1):
            return float(nums[0])
        current_sum = sum(nums[:k])
        maxi = current_sum
        for i in range(k,n):
            current_sum += nums[i]-nums[i-k]
            maxi = max(maxi, current_sum)
        return maxi/k
