class Solution:
    ans = 0
    def getMaximumGold(self, grid: List[List[int]]) -> int:
       def maxGold(row,col,n,m,gold,grid):
           if(row<0 or col<0 or row>=n or col>=m):
            return False
           if(grid[row][col]==0):
            return False
           gold += grid[row][col]
           Solution.ans = max(Solution.ans,gold)
           temp = grid[row][col]
           grid[row][col]=0
           maxGold(row+1,col,n,m,gold,grid)
           maxGold(row-1,col,n,m,gold,grid)
           maxGold(row,col-1,n,m,gold,grid)
           maxGold(row,col+1,n,m,gold,grid)
           grid[row][col] = temp
           gold -= temp
           return gold
       n = len(grid)
       m = len(grid[0])
       Solution.ans = 0
       for i in range(n):
        for j in range(m):
            gold = maxGold(i,j,n,m,0,grid)
       
       res = Solution.ans
       return res



