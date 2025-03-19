class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        dp =[[ [0]*(n+1) for _ in range(m+1)]for _ in range(len(strs)+1)]
        
        for i in range(1,len(strs)+1):
            zeros, ones = strs[i - 1].count('0'), strs[i - 1].count('1')
            for j in range(0,m+1):
                for k in range(0,n+1):
                    dp[i][j][k] = dp[i-1][j][k]
                    if j>=zeros and k>=ones:
                        dp[i][j][k] = max(dp[i][j][k],dp[i-1][j-zeros][k-ones]+1)
        return dp[len(strs)][m][n]

if __name__ == '__main__':
    solution = Solution()
    # strs = ["10","0001","111001","1","0"]
    # m = 5
    # n = 3
    # print(solution.findMaxForm(strs,m,n))
    # strs = ["10","0","1"]
    # m = 1
    # n = 1
    # print(solution.findMaxForm(strs,m,n))
    # strs = ["10","0001","111001","1","0"]
    # m = 4
    # n = 3
    # print(solution.findMaxForm(strs,m,n))
    strs = ["00101011"]
    m = 36
    n = 39
    print(solution.findMaxForm(strs,m,n))
    # #Output of this code is 4,2,3