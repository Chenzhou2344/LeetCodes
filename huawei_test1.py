def minimum_test_cases():
    # 读取输入
    n, m = map(int, input().split())  # n个测试用例，m个代码模块
    
    # 读取每个测试用例的覆盖情况
    cases = []
    for i in range(n):
        coverage = list(map(int, input().split()))
        cases.append(coverage)
    
    # 贪心算法：每次选择覆盖最多未覆盖模块的测试用例
    selected = []
    covered = [False] * m  # 标记每个模块是否被覆盖
    
    while not all(covered):
        best_case_idx = -1
        max_new_covered = -1
        
        # 查找能覆盖最多未覆盖模块的测试用例
        for i in range(n):
            if i in selected:
                continue
                
            new_covered = 0
            for j in range(m):
                if not covered[j] and cases[i][j] == 1:
                    new_covered += 1
            
            if new_covered > max_new_covered:
                max_new_covered = new_covered
                best_case_idx = i
        
        # 如果没有测试用例能覆盖新模块，则无法完全覆盖
        if max_new_covered == 0:
            return -1
        
        # 添加选中的测试用例，并更新覆盖状态
        selected.append(best_case_idx)
        for j in range(m):
            if cases[best_case_idx][j] == 1:
                covered[j] = True
    
    return len(selected)

# 主函数
if __name__ == "__main__":
    # 直接在代码中提供测试样例1的输入
    import io
    import sys
    
    # 将样例输入重定向到标准输入
    test_input = "3 4\n1 0 1 0\n0 1 0 1\n1 1 0 0"
    sys.stdin = io.StringIO(test_input)
    
    result = minimum_test_cases()
    print(result)
    
    # 测试样例2可以这样添加
    # test_input = "3 3\n1 0 0\n0 1 0\n0 0 0"
    # sys.stdin = io.StringIO(test_input)
    # result = minimum_test_cases()
    # print(result)