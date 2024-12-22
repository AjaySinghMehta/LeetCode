class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n =len(nums)
        uniques = set()
        i , j = 0 , 0
        while(j<n):
            if(nums[j] in uniques):
                return True
            uniques.add(nums[j])
            if(j-i+1<k+1):
                j+=1
            else:
                uniques.remove(nums[i])
                i += 1
                j += 1
        return False