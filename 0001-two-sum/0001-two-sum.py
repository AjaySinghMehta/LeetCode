# using dicitonaries faster than O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i , num in enumerate(nums):
            if target - num in visited:
                return (visited[target - num], i)  
            elif num not in visited:
                visited[num] = i
                  

            
            
