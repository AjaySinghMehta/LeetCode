class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        n = len(prices)
        result = prices[:]  # Start with the original prices as the result
        
        for i in range(n - 1, -1, -1):  # Traverse from right to left
            while stack and prices[stack[-1]] > prices[i]:  # Remove elements that are greater than prices[i]
                stack.pop()
            
            if stack:
                result[i] = prices[i] - prices[stack[-1]]  # Apply the discount
            stack.append(i)  # Add the current index to the stack
        
        return result