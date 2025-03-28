class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        diff = [g - c for g, c in zip(gas, cost)]
        current = 0
        start = 0
        total = 0
        for i, d in enumerate(diff):
            total += d 
            current += d
            if current < 0:
                start = i + 1
                current = 0
        return start if total >= 0 else -1
    
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