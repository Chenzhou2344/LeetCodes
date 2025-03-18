class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        sum_ = sum(nums)
        if sum_ % 2 != 0:
            return False
        dp = [[False]*(1+sum_//2) for _ in range(len(nums))]
        #init dp
        for i in range(len(nums)):
            dp[i][0] = True
        #mark this line i didnt init correctly
        if nums[0] <= sum_//2:
            dp[0][nums[0]] = True

        for i in range(1, len(nums)):
            for j in range(1, (sum_//2)+1):
                if j < nums[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
        return dp[-1][-1]

if __name__=='__main__':
    nums = [1, 5, 11, 5]
    solution = Solution()
    print(solution.canPartition(nums)) # True
    nums = [1, 2, 3, 5]
    print(solution.canPartition(nums)) # False
    nums = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]
    print(solution.canPartition(nums)) # False

