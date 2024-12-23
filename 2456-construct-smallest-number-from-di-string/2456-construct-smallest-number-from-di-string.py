class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        result = []
        num = list(range(1, len(pattern) + 2))
        
        for i, p in enumerate(pattern + 'I'):  
            stack.append(num[i])
            if p == 'I':
                while stack:
                    result.append(str(stack.pop()))
                    
        return ''.join(result)
