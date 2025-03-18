class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*(n+1)
        for i in range(2,n+1):
            for j in range(1,i):
                dp[i] = max(dp[i],max(j*(i-j),j*dp[i-j]))
        return dp[n]

if __name__ == "__main__":
    s = Solution()
    print(s.integerBreak(2))
    print(s.integerBreak(10))
    print(s.integerBreak(58))
    # Output:
    # 1
    # 36
    # 1549681956