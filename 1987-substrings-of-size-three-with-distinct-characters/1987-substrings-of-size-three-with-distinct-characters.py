class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)-2):
            print(s[i],s[i+1], s[i+2])
            if(s[i]!=s[i+1]):
                if(s[i] != s[i+2]):
                    if(s[i+1]!=s[i+2]):
                        count += 1
                        print("answers",s[i],s[i+1],s[i+2])
        return count

