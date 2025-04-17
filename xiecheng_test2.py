def max_profit():
    # 读取工人数量n和任务数量m
    n, m = map(int, input().split())
    
    # 读取工人的能力值
    worker_abilities = list(map(int, input().split()))
    
    # 读取任务所需的能力值
    task_requirements = list(map(int, input().split()))
    
    # 读取任务的收益值
    task_profits = list(map(int, input().split()))
    
    total_profit = 0
    
    # 对于每个工人，找出他能完成的任务中收益最大的
    for ability in worker_abilities:
        max_profit_for_worker = 0
        
        # 检查每个任务
        for i in range(m):
            # 如果工人能力值大于等于任务所需能力值
            if ability >= task_requirements[i]:
                # 更新这个工人可以获得的最大收益
                max_profit_for_worker = max(max_profit_for_worker, task_profits[i])
        
        # 将这个工人的最大收益加到总收益中
        total_profit += max_profit_for_worker
    
    return total_profit

# 读取测试用例数量
t = int(input())

# 处理每个测试用例
for _ in range(t):
    result = max_profit()
    print(result)