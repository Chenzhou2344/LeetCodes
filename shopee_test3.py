class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        # Initialize the sum of the first 'k' elements
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Slide the window through the array
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)
        
        # Calculate and return the maximum average
        return max_sum / k