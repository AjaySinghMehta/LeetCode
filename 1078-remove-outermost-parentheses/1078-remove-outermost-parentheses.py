class Solution:
    def removeOuterParentheses(self, s: str) -> str:
    
        stack = []
        result = []

        for i in range(len(s)):
            if s[i] == '(':
                if stack:
                    result.append(s[i])
                stack.append('(')
            elif s[i] == ')':
                stack.pop()
                if stack:
                    result.append(s[i])

        return ''.join(result)

