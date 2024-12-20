class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        dict = {}
        maxi = 0

        for r in range(n):
            # Add the current character to the frequency dictionary
            if s[r] in dict:
                dict[s[r]] += 1
            else:
                dict[s[r]] = 1
            
            # Shrink the window if any character occurs more than twice
            while any(freq > 2 for freq in dict.values()):
                dict[s[l]] -= 1
                if dict[s[l]] == 0:
                    del dict[s[l]]
                l += 1
            
            # Update the maximum length of the valid substring
            maxi = max(maxi, r - l + 1)
        
        return maxi