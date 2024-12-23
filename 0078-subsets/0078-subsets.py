class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def dfs(index, path):
            if index == len(nums):
                result.append(path)
                return
           
            dfs(index + 1, path + [nums[index]])
            
            dfs(index + 1, path)
        
        dfs(0, [])
        return result

        