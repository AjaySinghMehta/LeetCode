class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        # brute force
        n = len(s)
        maxi = ""
        temp = []
        for i in range(n):
            for j in range(i+1,n+1):
                temp.append(s[i:j])
        t = []
        for i in temp:
            flag = 0
            for j in range(len(i)):
                if chr(ord(i[j]) - 32) in i or chr(ord(i[j]) + 32) in i:
                   flag = 1
                else:
                    flag = 0
                    break
            if(flag and len(maxi)<len(i)):
                maxi = i
        print(temp)
        return maxi

                