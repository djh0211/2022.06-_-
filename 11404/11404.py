import sys
input = sys.stdin.readline
INF = int(1e9)
n=int(input())
m=int(input())

bus_cost = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(m):
    start,end,cost = map(int, input().split())
    bus_cost[start][end] = min(cost, bus_cost[start][end])

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                bus_cost[i][j] = 0
            else:
                bus_cost[i][j] = min(
                    bus_cost[i][j],
                    bus_cost[i][k]+bus_cost[k][j]
                    )

for row in bus_cost[1:]:
    for col in row[1:]:
        if col == INF:
            print(0, end = " ")
        else:
            print(col, end = " ")
    print()
