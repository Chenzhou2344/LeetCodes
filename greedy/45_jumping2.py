class Solution:
    def jump(self, nums: list[int]) -> int:
        jumpsteps = [len(nums)+1]*len(nums)
        jumpsteps[0] = 0
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            for j in range(i,min(i+nums[i]+1,len(jumpsteps))):
                jumpsteps[j] = min(jumpsteps[j],jumpsteps[i]+1)

        return jumpsteps[-1]

#faster solution
# class Solution:
#     def jump(self, nums: list[int]) -> int:
#         if len(nums) == 1:
#             return 0
#         max_distance = nums[0]
#         min_jump = 0
#         end = 0
#         l = len(nums)
#         for i in range(l-1):
#             if max_distance>=i:
#                 max_distance = max(max_distance,nums[i]+i)
#                 if i == end:
#                     min_jump+=1
#                     end = max_distance

#         return min_jump

if __name__ == '__main__':
    nums = [2,3,1,1,4]
    s = Solution()
    print(s.jump(nums))#2
    nums = [2,3,0,1,4]
    print(s.jump(nums))#2
    nums = [0]
    print(s.jump(nums))#0
    nums = [1,2,3]
    print(s.jump(nums))#2