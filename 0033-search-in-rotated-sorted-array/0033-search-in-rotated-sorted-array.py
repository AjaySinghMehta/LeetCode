from collections import deque
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0 
        r = n-1
        mid = (l+r)//2
        while(l <= mid or r>=mid ):
            if(nums[mid] == target):
                return mid
            if(nums[l]==target):
                return l
            if(nums[r]==target):
                return r
            l+=1
            r-=1
        return -1