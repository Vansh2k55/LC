class Solution:
    def bestClosingTime(self, customers: str) -> int:
        count=defaultdict(int)
        for i in range(len(customers)):
            if customers[i]=='Y':
                count['Y']+=1
            
        penalty=count['Y']
        ans=0
        for i in range(len(customers)):
            if customers[i]=='Y':
                count['Y']-=1
            else:
                count['N']+=1
            newpen=count['Y']+count['N']
            if newpen<penalty:
                penalty=newpen
                ans=i+1
        return ans

        