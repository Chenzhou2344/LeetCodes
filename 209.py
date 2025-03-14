class Solution:
    def minSubArrayLen(self, s: int, nums: list[int]) -> int:
        l = len(nums)
        left = 0
        right = 0
        min_len = float('inf')
        cur_sum = 0 #当前的累加值
        
        while right < l:
            cur_sum += nums[right]
            
            while cur_sum >= s: # 当前累加值大于目标值
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1
            
            right += 1
        
        return min_len if min_len != float('inf') else 0
    
if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(7, [2,3,1,2,4,3])) # 2
    # print(s.minSubArrayLen(4, [1,4,4])) # 1
    print(s.minSubArrayLen(11, [1,1,1,1,1,1,1])) # 11
