class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(start, target, current_combination):
            if target == 0:
                result.append(list(current_combination))
                return
            for i in range(start, len(candidates)):
                if candidates[i] <= target:
                    current_combination.append(candidates[i])
                    backtrack(i, target - candidates[i], current_combination)
                    current_combination.pop()

        backtrack(0, target, [])
        return result

        