class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        dp = [999]*(len(cost)+1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2,len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])

        return dp[-1]
if __name__ == '__main__':
    s = Solution()
    print(s.minCostClimbingStairs([10, 15, 20]))
    print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
    print(s.minCostClimbingStairs([0,0,0,1]))
    # Output:
    # 15
    # 6
    # 0