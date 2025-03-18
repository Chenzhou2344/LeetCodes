class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0]==1:
                dp[i][0] = 0
                break
            dp[i][0] = (1-obstacleGrid[i][0])
        for ii in range(i+1,m):
            dp[ii][0] = 0

        for j in range(n):
            if obstacleGrid[0][j]==1:
                dp[0][j] = 0
                break
            dp[0][j] = (1-obstacleGrid[0][j])
        for jj in range(j+1,n):
            dp[0][jj] = 0

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = (dp[i-1][j]+dp[i][j-1])*(1-obstacleGrid[i][j])
        
        print(dp)
        
        return dp[-1][-1]
if __name__ == '__main__':
    s = Solution()
    print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
    print(s.uniquePathsWithObstacles([[0,1],[0,0]]))
    # Output:
    # 2
    # 1