class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        sum_ = sum(nums)
        if sum_ % 2 != 0:
            return False
        dp  = [0]*(sum_//2+1)
        for num in nums:
            for j in range(sum_//2,num-1,-1):
                dp[j] = max(dp[j],dp[j-num]+num)
        if sum_//2 == dp[sum_//2]:
            return True
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    print(s.canPartition([1, 5, 11, 5]))