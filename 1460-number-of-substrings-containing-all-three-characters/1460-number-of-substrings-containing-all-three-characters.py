class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d = {char : 0 for char in 'abc'}
        l = 0
        n = len(s)
        result = 0
        for r in range(n):
            d[s[r]] += 1
            while all(d[char]>0 for char in 'abc'):
                result += n-r
                d[s[l]] -= 1
                l += 1
        return result

        
            
        