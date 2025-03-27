class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        day_profit = [0]*len(prices)
        lowest_price = prices[0]
        for i in range(1,len(prices)):
            if prices[i] < lowest_price:
                lowest_price = prices[i]
            day_profit[i] = prices[i] - lowest_price
        return max(day_profit)
        
    
if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    solution = Solution()
    print(solution.maxProfit(prices)) #5
    prices = [7,6,4,3,1]
    print(solution.maxProfit(prices)) #0
    prices = [1,2,3,4,5]
    print(solution.maxProfit(prices)) #4
