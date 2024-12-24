class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        heapq.heapify(nums)
        while len(nums) > 1:
            n1 = heapq.heappop(nums)
            n2 = heapq.heappop(nums)
            arr.extend([n2, n1])
        if len(nums) != 0:
            n1 = heapq.heappop(nums)
            arr.append(n1)
        return arr