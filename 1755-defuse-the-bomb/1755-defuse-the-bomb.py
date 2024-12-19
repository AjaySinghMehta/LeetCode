class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans = []
        if(k == 0):
            return [0]*len(code)
        for i in range(len(code)):
            curr_sum = 0
            if(k>0):
                for j in range(i+1,i+k+1):
                    l = (j)%len(code)
                    curr_sum += code[l]
            else:
                temp = abs(k)
                for  j in range(1, temp+1):
                    l = (i+len(code)-j)%len(code)
                    curr_sum += code[l]
            ans.append(curr_sum)
        return ans

                
        
        