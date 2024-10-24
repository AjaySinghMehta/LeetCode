class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def solution(index):
            if(index == n):
                res.append(nums[:])
            for i in range(index,n):
                nums[index], nums[i] = nums[i], nums[index]
                solution(index+1)
                nums[index], nums[i] = nums[i], nums[index]
        solution(0)
        return res
