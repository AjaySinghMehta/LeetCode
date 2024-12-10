class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        left = 0
        right = 0
        count = 0
        sum = 0
        while(right<n and goal!= 0 ):
            sum += nums[right]
            while(sum > goal and left <= right):
                sum -= nums[left]
                left += 1
            if(sum == goal):
                count += 1
                temp = left
                while(temp < right and nums[temp]==0):
                    count += 1
                    temp += 1
           
            right += 1
        if(goal == 0):
            zero_count = 0
            for num in nums:
                if(num == 0):
                    zero_count += 1
                else:
                    count += zero_count * (zero_count + 1) // 2
                    zero_count = 0
            count += zero_count * (zero_count + 1)//2 
       
        return count
            

            
            

            