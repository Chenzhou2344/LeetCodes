class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        diff = [g - c for g, c in zip(gas, cost)]
        diff = dict(enumerate(diff))
        diff = sorted(diff.items(), key=lambda x: x[1])
        current = 0
        for i in range(len(diff)):
            current += diff[i][1]
            if current < 0:
                return -1
        return diff[0][0]