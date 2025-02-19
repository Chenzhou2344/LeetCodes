class Solution:
    def search(self, nums: list[int], target: int) -> int:
        length = len(nums) - 1

        def bis(left, right):
            mid =int( (left + right) / 2)
            print(f"left: {left}, right: {right}, mid: {mid}")
            if nums[mid] == target:
                return mid
            elif left == right:
                return -1
            elif nums[mid] < target and nums[right] >= target:
                return bis(mid, right)
            else:
                return bis(left, mid - 1)

        return bis(0, length)

    
if __name__ == "__main__":
    solution = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    result = solution.search(nums, target)
    print(f"Index of target {target} is: {result}")