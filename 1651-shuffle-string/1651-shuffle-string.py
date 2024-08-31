class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        li = list(s)
        res = [0]*len(indices)
        for i in range(len(indices)):
            res[indices[i]] = li[i]
        result = ""
        
        result = result.join(res)
        return result
        