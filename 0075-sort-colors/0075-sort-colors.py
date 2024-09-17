class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        one = 0
        two = 0
        three = n-1
        # while(nums[three]==2):
        #     three -= 1
        while(two<=three):
            if(nums[two]==0):
            #if num[one]==0 
            # swap -> two+=1
                temp = nums[two]
                nums[two] = nums[one]
                nums[one] = temp
                two += 1
                one += 1
            elif(nums[two]==1):
                two+=1
            else:
                nums[two], nums[three] = nums[three], nums[two]
                three -= 1
     