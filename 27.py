# class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:
#         length = len(nums)
#         conut = 0
#         i = 0
#         while i < length:
#             if nums[i] == val:
#                 conut += 1
#                 for j in range(i+1, length):
#                     nums[j-1] = nums[j]
#                 i = i-1
#                 length = length - 1
#             i += 1
#             print(nums)
#         print(conut)
#         return len(nums)-conut
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        size = len(nums)
        index1 = 0
        index2 = 0
        while index1 < size:
            if nums[index1] != val:
                nums[index2]=nums[index1]
                index2+=1
            index1+=1
        return index2

        
if __name__ == "__main__":
    solution = Solution()
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    result = solution.removeElement(nums, val)
    print(f"Length of new array after removing {val} is: {result}")

        