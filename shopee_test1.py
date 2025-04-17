class solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while stack and k > 0 and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)
        if k > 0:
            stack = stack[:-k]
        return ''.join(stack).lstrip('0') or '0'

if __name__ == "__main__":
    # Example usage:
    num = "1432219"
    k = 3

    s = solution()
    result = s.removeKdigits(num, k)
    print(result)  # Output: "1219"