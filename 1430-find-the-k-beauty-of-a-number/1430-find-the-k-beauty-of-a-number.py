class Solution:
    def is_beauty(num , sub):
        if(sub == 0):
            return False
        if(num%sub == 0):
            return True
        else:
            return False

    def divisorSubstrings(self, num: int, k: int) -> int:
        # print(Solution.is_beauty(240,24))
        num_s = str(num)
        count = 0
        if(len(num_s)==1):
            return 1
        for i in range(len(num_s)-k+1):
                temp = num_s[i:i+k]
                print(int(temp))
                if(Solution.is_beauty(num, int(temp))):
                    count+=1
        return count
