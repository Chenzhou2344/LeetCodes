class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        sum_ = sum(nums)
        dp = [[0]*(2*sum_+1) for _ in range(len(nums))]
        if sum_ < abs(target):
            return 0
        #init dp
        dp[0][nums[0]+sum_] = 1
        dp[0][-nums[0]+sum_] += 1
        for i in range(len(nums)):
            dp[i][2*sum_] = 1
            dp[i][0] = 1
            
        for i in range(1, len(nums)):
            for j in range(2*sum_+1):
                jj = j-sum_
                if jj - nums[i] > -sum_:
                    dp[i][j] += dp[i-1][j-nums[i]]
                if jj + nums[i] < sum_:
                    dp[i][j] += dp[i-1][j+nums[i]]
        return dp[-1][target+sum_]

if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1]
    target = 3 
    solution = Solution()
    print(solution.findTargetSumWays(nums, target)) # 5
    nums = [1]
    target = 1
    print(solution.findTargetSumWays(nums, target)) # 1
    nums = [1]
    target = 2
    print(solution.findTargetSumWays(nums, target)) # 0