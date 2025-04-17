def can_decompose(n, m):
    """
    检查是否能将正整数n分解为m个连续的非负整数
    """
    # 如果序列从a开始，那么有：
    # a + (a+1) + (a+2) + ... + (a+m-1) = n
    # 展开得到：m*a + (0+1+2+...+m-1) = n
    # 等差数列求和：m*a + (m-1)*m/2 = n
    # 解得：a = (n - (m-1)*m/2) / m
    
    # 计算等差数列和：0+1+2+...+(m-1)
    arithmetic_sum = (m - 1) * m // 2
    
    # 计算起始数字a
    a = (n - arithmetic_sum) / m
    
    # 检查a是否为非负整数
    return a.is_integer() and a >= 0

def main():
    # 示例测试用例
    test_cases = [
        (9, 3),
        (8, 2),
        (15, 5),
        (10, 4)
    ]
    
    # 处理每个测试用例
    for n, m in test_cases:
        if can_decompose(n, m):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()