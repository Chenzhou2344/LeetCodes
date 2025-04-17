import sys
from collections import defaultdict, deque

input = sys.stdin.readline

n = int(input())
lines = []
station_to_lines = defaultdict(set)
graph = defaultdict(list)

# 建图 & 站点-线路映射
for line_id in range(n):
    stations = input().strip().split()
    lines.append(stations)
    for i in range(len(stations)):
        station_to_lines[stations[i]].add(line_id)
        if i > 0:
            u, v = stations[i - 1], stations[i]
            graph[u].append((v, line_id))
            graph[v].append((u, line_id))

start, end = input().strip().split()

if start == end:
    print(start)
    print(2)
    sys.exit(0)

# BFS: 当前站，当前线路，路径（只存换乘点），换乘次数
queue = deque()
visited = set()

for line_id in station_to_lines[start]:
    # 起点加入路径
    queue.append((start, line_id, [start], 0))
    visited.add((start, line_id))

found = False

while queue:
    station, cur_line, path, transfer_count = queue.popleft()

    if station == end:
        if path[-1] != end:
            path.append(end)
        print('-'.join(path))
        print(2 + transfer_count)
        found = True
        break

    for neighbor, next_line in graph[station]:
        next_transfer = transfer_count
        new_path = list(path)

        if next_line != cur_line:
            # 换乘，记录换乘点
            next_transfer += 1
            new_path.append(station)

        state = (neighbor, next_line)
        if state not in visited:
            visited.add(state)
            queue.append((neighbor, next_line, new_path, next_transfer))

if not found:
    print("NA")
