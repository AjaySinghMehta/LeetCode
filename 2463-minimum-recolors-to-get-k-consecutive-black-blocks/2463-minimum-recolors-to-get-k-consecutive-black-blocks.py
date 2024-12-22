class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i = 0
        n = len(blocks)
        count = 100
        while(i+k<=n):
            temp = blocks[i:i+k]
            t_count = 0
            for j in temp:
                if(j=="W"):
                    t_count+=1
            count = min(t_count,count)
            i+=1
        return count

                    
        
        