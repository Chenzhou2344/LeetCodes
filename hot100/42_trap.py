class Solution:
    def trap(self, height: list[int]) -> int:
        pre = 0
        post = 2
        n = len(height)
    
        while post<n: