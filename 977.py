class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        index_posi = len(nums) - 1
        index_nega = 0
        sqare = [0] * len(nums)
        max2min = len(nums) - 1
        while max2min>=0:
            if nums[index_posi] ** 2 > nums[index_nega] ** 2:
                sqare[max2min] = nums[index_posi] ** 2
                max2min = max2min - 1
                index_posi = index_posi - 1
            else:
                sqare[max2min] = nums[index_nega] ** 2
                max2min = max2min - 1
                index_nega = index_nega + 1
        return sqare
