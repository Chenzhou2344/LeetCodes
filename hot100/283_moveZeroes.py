class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pre = 0
        post = 0
        len_nums = len(nums)
        if len_nums == 1:
            print(nums)
        else:
            while(post<len_nums and pre<=post):
                print(f"pre: {pre}, post: {post}, nums: {nums},nums[pre]: {nums[pre]}, nums[post]: {nums[post]}")
                if nums[pre]==0 and nums[post]!=0:
                    nums[pre] = nums[post]
                    nums[post] = 0
                    post+=1
                    pre+=1
                elif nums[pre]==0 and nums[post]==0:
                    post+=1
                elif nums[pre]!=0 and nums[post]==0:
                    post+=1
                    pre+=1
                elif nums[pre]!=0 and nums[post]!=0:
                    if pre==post:
                        post+=1
                        pre+=1
                    else:
                        pre+=1
            
            print(nums)

if __name__ == '__main__':
    s = Solution()
    s.moveZeroes([0,1,0,3,12]) # Output: [1,3,12,0,0]
    s.moveZeroes([0])           # Output: [0]
    s.moveZeroes([1])           # Output: [1]
    s.moveZeroes([0,0,1])      # Output: [1,0,0]
    s.moveZeroes([1,0,1])      # Output: [1,1,0]
