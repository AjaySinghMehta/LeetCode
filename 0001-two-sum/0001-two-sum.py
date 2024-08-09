
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #using dobule for loop brute force
        # for i in range(0,len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return i,j
        # return -1
        
        # using dicitonaries faster than O(n^2)
        visited = {}
        for i , num in enumerate(nums):
            if target - num in visited:
                return (visited[target - num], i)  
            elif num not in visited:
                visited[num] = i
                  

            
            
