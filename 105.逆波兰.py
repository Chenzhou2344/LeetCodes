class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for i in tokens:
            if i in ['+', '-', '*', '/']:
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    stack.append(a + b)
                elif i == '-':
                    stack.append(a - b)
                elif i == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(i))
        return stack[0]

if __name__ == '__main__':
    tokens = ["2", "1", "+", "3", "*"]  
    solution = Solution()
    print(solution.evalRPN(tokens))  # Output: 9