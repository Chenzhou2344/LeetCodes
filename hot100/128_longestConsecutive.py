class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        numset = set(nums)
        if len(numset) == 0:
            return 0
        maxlen = 0

        for num in numset:
            if num-1 not in numset:
                lens = 1
                index = num
                
                while index+1 in numset:
                    index+=1
                    lens+=1
                
                maxlen = max(maxlen,lens)
        return maxlen
if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    sol = Solution()
    print(sol.longestConsecutive(nums))  # Output: 4 (The longest consecutive elements sequence is [1, 2, 3, 4])
    nums = [0, 0, 1]
    print(sol.longestConsecutive(nums))  # Output: 2 (The longest consecutive elements sequence is [0, 1])
    nums = [1, 2, 0, 1]
    print(sol.longestConsecutive(nums))  # Output: 3 (The longest consecutive elements sequence is [0, 1, 2])
    nums = [0,-1]
    print(sol.longestConsecutive(nums))  # Output: 2 (The longest consecutive elements sequence is [-1, 0])

