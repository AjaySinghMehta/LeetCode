class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        maxi = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if(abs(nums[i]-nums[j])<=min(nums[i], nums[j])):
                    xor = nums[i]^nums[j]
                    maxi = max(maxi, xor)
                    
        return maxi
