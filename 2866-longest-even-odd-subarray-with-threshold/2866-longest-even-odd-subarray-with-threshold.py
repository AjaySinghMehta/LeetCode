class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        l = 0
        maxlength = 0 
        while(l<n):
            if(nums[l]%2!= 0 or threshold < nums[l]):
                l += 1
                continue
            r = l
            while(r<n and nums[r]<=threshold and (r == l or nums[r]%2 != nums[r-1]%2)):
                r += 1
            maxlength = max(maxlength, r-l)
            l += 1
        return maxlength

                
                
                
                 


