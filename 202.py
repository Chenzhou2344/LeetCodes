class Solution:
    def isHappy(self, n: int) -> bool:
        history_set = set()
        def sum(n:int)->int:
            new_num = 0
            while(n!=0):
                new_num = new_num + (n%10)**2
                n = n//10
            return new_num
        new_num = sum(n)
        while(new_num!=1):
            print(new_num)
            if new_num in history_set:
                return False
            else:
                history_set.add(new_num)
                new_num = sum(new_num)
        return True

if __name__ == '__main__':
    n = 19
    solution = Solution()
    print(solution.isHappy(n))