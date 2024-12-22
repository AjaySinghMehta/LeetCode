class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: float) -> int:
        l = 0 
        count = 0
        n = len(nums)
        if(n == 1):
            if(nums[0]>=threshold):
                return 1
            else:
                return 0
        # while(l<=n-k):
        #     current_sum = 0
        #     for r in range(l,l+k):
        #         current_sum += nums[r]
        #     if((current_sum/k)>=threshold):
        #         count += 1
        #     l+=1
        current_sum = 0
        for i in range(k):
            current_sum += nums[i]
        if(current_sum/k)>= threshold:
            count += 1
        for i in range(k, n):
            current_sum  += nums[i] - nums[i-k]
            if(current_sum / k >= threshold):
                count += 1
        return count

        
        return count
            

            