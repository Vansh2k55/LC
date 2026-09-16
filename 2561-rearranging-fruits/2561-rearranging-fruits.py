class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        c1=Counter(basket1)
        c2=Counter(basket2)
        total=c1+c2
        for x in total:
            if total[x]%2!=0:
                return -1
        mn=min(min(basket1),min(basket2))
        extra1=[]
        extra2=[]
        for x in c1:
            diff=c1[x]-c2[x]
            if diff>0:
                extra1.extend([x]*(diff//2))
        for x in c2:
            diff=c2[x]-c1[x]
            if diff>0:
                extra2.extend([x]*(diff//2))
        extra1.sort()
        extra2.sort(reverse=True)
        ans=0
        for x,y in zip(extra1,extra2):
            ans+=min(min(x,y),mn*2)
        return ans

        