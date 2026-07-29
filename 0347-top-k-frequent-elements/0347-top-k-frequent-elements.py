import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=Counter(nums)
        heap=[]
        for m,v in counter.items():
            heapq.heappush(heap,(v,m))
            if len(heap)>k:
                heapq.heappop(heap)
        return [m for v,m in heap]
        