#自己的解法
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        coverrange = nums[0]
        index = 0

        while index <= coverrange and index < len(nums):
            coverrange = max(coverrange, index + nums[index])
            index += 1
            print(index, coverrange)

        if coverrange >= len(nums)-1:
            return True
        return False
    
#代码随想录解法
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         cover = 0
#         if len(nums) == 1: return True
#         i = 0
#         # python不支持动态修改for循环中变量,使用while循环代替
#         while i <= cover:
#             cover = max(i + nums[i], cover)
#             if cover >= len(nums) - 1: return True
#             i += 1
#         return False

if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    solution = Solution()
    print(solution.canJump(nums))
    nums = [3, 2, 1, 0, 4]
    print(solution.canJump(nums))
    nums = [1,2,3]
    print(solution.canJump(nums))