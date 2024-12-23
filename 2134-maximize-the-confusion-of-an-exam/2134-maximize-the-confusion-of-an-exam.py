class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        def longest_with_char(target: str)->int:
            l = 0
            count = 0
            max_length = 0
            for r in range(n):
                if(answerKey[r] != target):
                    count += 1
                
                while(count > k):
                    if(answerKey[l]!= target):
                        count -= 1
                    l += 1
                
                max_length = max(max_length, r-l+1)
            return max_length
        max_t = longest_with_char('T')
        max_f = longest_with_char('F')
        return max(max_t, max_f) 