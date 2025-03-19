class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [[0]*(amount+1) for _ in range(len(coins)+1)] 
        for j in range(amount+1):
            dp[0][j] = 0
        for i in range(len(coins)+1):
            dp[i][0] = 1
        for i in range(1,len(coins)+1):
            for j in range(1,amount+1):
                dp[i][j] = dp[i-1][j]
                if j >= coins[i-1]:
                    dp[i][j] += dp[i][j-coins[i-1]]
        return dp[len(coins)][amount]
    
if __name__=='__main__':
    solution = Solution()

    amount = 5  
    coins = [1, 2, 5]
    print(solution.change(amount, coins)) # 4
    amount = 3
    coins = [2]
    print(solution.change(amount, coins)) # 0
    amount = 10
    coins = [10]
    print(solution.change(amount, coins)) # 1