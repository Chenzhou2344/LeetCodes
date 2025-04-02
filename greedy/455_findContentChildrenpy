class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        s.sort(reverse=True)
        g.sort()
        Satasified = 0
        for cake in s:
            while g and cake < g[-1]:
                g.pop()
            if g and cake >= g[-1]:
                g.pop()
                Satasified += 1

        return Satasified
    
if __name__ == '__main__':
    g = [1, 2, 3]
    s = [1, 1]
    solution = Solution()
    print(solution.findContentChildren(g, s))  # Output: 1
    g = [1, 2]
    s = [1, 2, 3]
    print(solution.findContentChildren(g, s))  # Output: 2
    g = [10, 9, 8, 7]
    s = [5, 6, 7, 8]
    print(solution.findContentChildren(g, s))  # Output: 2