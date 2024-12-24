class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
		#    First, import the heapq module. Specifically the functions heapify, heappop and heappush
        from heapq import heapify, heappop, heappush
        
		#    Initialize an empty array, which we would use as heap
        heap = []
        for stone in stones:
		
		#    We would add the negative values of the given list in the Heap
            heap.append(-stone)
        
		#    heapify function from the heapq module, takes an array as parameter, arranges the contents
		#    of the array in such a way that the array becomes a minheap
        heapify(heap)
        
        while len(heap) > 1:
		
		#    heappop function from the heapq module, takes an array (heap) as parameter, and removes
		#    the root of the minheap, returns the value, and then makes the necessary arrangement so
		#    that the heap does not lose its properties.
            x = heappop(heap)
            y = heappop(heap)
            
		#    if the two minimum values from the heap are not equal, then subtract the larger value (smaller
		#    magnitude) from the smaller value (larger magnitude). Add the difference back to the heap
            if x != y:
			
		#    heappush function, from the heapq module, takes an array (heap) as parameter, and adds
		#    the second parameter to the array, maintaining the heap properties of the array.
                heappush(heap, x - y)
        
		#    if heap is not empty then, return the first item in the heap multiplied by -1
        if heap:
            return -heap[0]
			
		#    if heap was empty, then return 0
        return 0