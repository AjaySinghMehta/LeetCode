class Solution:
    def seq(num):
        if(num == 0):
            return 0
        elif(num == 1):
            return 1
        else:
            return Solution.seq(num-1)+ Solution.seq(num-2) 
    def fib(self, n: int) -> int:
        return Solution.seq(n)