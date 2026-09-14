class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        births = sorted([x[0] for x in logs])
        deaths = sorted([x[1] for x in logs])

        i = 0
        j = 0
        current = 0
        maxpeople = 0
        ans = 1950

        while i < len(births):
            if births[i] < deaths[j]:
                current += 1

                if current > maxpeople:
                    maxpeople = current
                    ans = births[i]

                i += 1
            else:
                current -= 1
                j += 1

        return ans