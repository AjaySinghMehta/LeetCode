class Solution:
    def maxDepth(self, s: str) -> int:
        # current_depth = 0
        max_depth = 0
        
        # for i in s:
        #     if(i == '('):
        #         current_depth += 1
        #         max_depth = max(max_depth, current_depth)
        #     elif(i == ')'):
        #         current_depth -= 1
        # return max_depth


        # using stack
        stack = []
        for i in s:
            if(i == '('):
                stack.append('(')
                # current_depth += 1
                max_depth = max(max_depth, len(stack))
            elif(i == ')'):
                stack.pop()

        return max_depth