class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
            print(dp)

        return dp[-1]
    

if __name__ == '__main__':
    nums = [1,2,3,1]
    print(Solution().rob(nums)) # 4

    nums = [2,7,9,3,1]
    print(Solution().rob(nums)) # 12

    nums = [2,1,1,2]
    print(Solution().rob(nums)) # 4