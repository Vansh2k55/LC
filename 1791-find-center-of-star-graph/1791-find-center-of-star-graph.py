from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n=len(edges)
        graph=defaultdict(int)
        for u,v in edges:
            graph[u]+=1
            graph[v]+=1
        for key,value in graph.items():
            if value==n:
                return key



        