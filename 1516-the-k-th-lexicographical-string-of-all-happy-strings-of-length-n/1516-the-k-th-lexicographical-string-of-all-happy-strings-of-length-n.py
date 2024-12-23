class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []
        
        def backtrack(current):
            if len(current) == n:
                result.append(current)
                return
            for char in 'abc':
                if not current or current[-1] != char:
                    backtrack(current + char)
        
        backtrack("")
        
        return result[k - 1] if k <= len(result) else ""
