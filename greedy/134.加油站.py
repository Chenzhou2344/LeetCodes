class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        diff = [g - c for g, c in zip(gas, cost)]
        diff = dict(enumerate(diff))
        diff = sorted(diff.items(), key=lambda x: x[1], reverse=True)
        current = 0
        for i in range(len(diff)):
            current += diff[i][1]
            if current < 0:
                return -1
        return diff[0][0]
    
if __name__ == '__main__':
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    solution = Solution()
    print(solution.canCompleteCircuit(gas, cost))
    gas = [2, 3, 4]
    cost = [3, 4, 3]
    print(solution.canCompleteCircuit(gas, cost))
    gas = [5, 1, 2, 3, 4]
    cost = [4, 4, 1, 5, 1]
    print(solution.canCompleteCircuit(gas, cost))
    gas = [2, 3, 4]
    cost = [3, 4, 4]
    print(solution.canCompleteCircuit(gas, cost))