class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        s = 1
        while s**2 <= n:
            squares.append(s**2)
            s += 1

        dp = [n+1]*(n+1)
        dp[0] = 0
        for i in range(len(squares)):
            for j in range(1,n+1):
                if j-squares[i]>=0:
                    dp[j] = min(dp[j],dp[j-squares[i]]+1)
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.numSquares(1))
    # print(s.numSquares(13))
    # Output for the above test cases are:
    # 3
    # 2