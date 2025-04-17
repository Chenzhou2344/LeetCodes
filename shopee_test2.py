class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        #select the range of the array to find the maximum product
        prefix_product = [1] * (len(nums) + 1)
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            prefix_product[i + 1] = product
        max_product = float('-inf')
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                max_product = max(max_product, prefix_product[j] // prefix_product[i])
        return max_product
    
if __name__ == "__main__":
    # Example usage:
    nums = [2, 3, -2, 4]
    
    s = Solution()
    result = s.maxProduct(nums)
    print(result)  # Output: