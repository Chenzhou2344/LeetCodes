class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        sum_ = sum(stones)
        dp = [[False]*(sum_+1) for _ in range(len(stones))]
        #init dp
        for i in range(len(stones)):
            dp[i][0] = True
        #mark this line i didnt init correctly
        dp[0][stones[0]] = True
        

        for i in range(1, len(stones)):
            for j in range(1, sum_+1):
                if j < stones[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-stones[i]]
        diff = sum_
        for j in range(sum_):
            if dp[-1][j]:
                diff = min(diff, abs(sum_-2*j))

        return diff
    
if __name__ == '__main__':
    stones = [2, 7, 4, 1, 8, 1]
    solution = Solution()
    print(solution.lastStoneWeightII(stones)) # 1
    stones = [31,26,33,21,40]
    print(solution.lastStoneWeightII(stones)) # 5
    stones = [1,2]
    print(solution.lastStoneWeightII(stones)) # 1
    stones = [1,2,3,4,5,6,7]
    print(solution.lastStoneWeightII(stones)) # 0