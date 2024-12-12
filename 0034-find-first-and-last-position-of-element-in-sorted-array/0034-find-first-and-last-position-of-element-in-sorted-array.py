class Solution:
    def firstpos(nums, target, n):
        l = 0
        r = n-1
        while(l<r):
            mid = (l+r)//2
            if(target<=nums[mid]):
                r = mid
            else:
                l = mid+1
            if(l == r and target!=nums[l]):
                return -1
            
        return l
    
    def lastpos(nums, target , n):
        l = 0 
        r = n-1
        while(l<r):
            mid = (l+r)//2
            if(nums[mid]<=target):
                l = mid+1
            else:
                r = mid
            if(l == r and target == nums[l]):
                return l
            elif(l==r and target != nums[l-1]):
                return -1
        return l-1
    
              

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        ans = []
        if(n > 1):
            ans.append(Solution.firstpos(nums, target, n))
            ans.append(Solution.lastpos(nums, target, n))
        elif(n == 0):
            return (-1,-1)
        elif(n == 1):
            if(target == nums[0]):
                return (0,0)
            else:
                return (-1,-1)
        return ans