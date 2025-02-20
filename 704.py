class Solution:
    def search(self, nums: list[int], target: int) -> int:
        length = len(nums) - 1
        def binary_search(nums, target, left, right):
            if left > right:
                return -1  # 递归终止条件，未找到目标值
            
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid  # 找到目标值，返回索引
            elif nums[mid] < target:
                return binary_search(nums, target, mid + 1, right)  # 递归右半部分
            else:
                return binary_search(nums, target, left, mid - 1)  # 递归左半部分
        return binary_search(nums, target, 0, length)
            
    
if __name__ == "__main__":
    solution = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    result = solution.search(nums, target)
    print(f"Index of target {target} is: {result}")