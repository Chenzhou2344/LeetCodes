class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        if amount == 0:
            return 0
        dp[0] = 0
        for i in range(len(coins)):
          for j in range(1,amount+1):
                if j-coins[i]>=0:   
                    dp[j] = min(dp[j],dp[j-coins[i]]+1)
        return dp[-1] if dp[-1]!=(amount+1) else -1
    
if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([1,2,5],11))
    print(s.coinChange([2],3))
    print(s.coinChange([1],0))
    print(s.coinChange([1],1))
    print(s.coinChange([1],2))
    print(s.coinChange([1,2,5],100))
    # Output for the above test cases are:
    # 3
    # -1
    # 0
    # 1
    # 2
    # 20
