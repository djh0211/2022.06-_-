cnt = 0
def solution(n, queryType, students1, students2):
    # Write your code here
    graph = [[]for _ in range(n+1)]
    
    def dfs(graph, v, visited):
        global cnt
        visited[v] = True
        cnt += 1
        for i in graph[v]:
            if not visited[i]:
                dfs(graph, i, visited)
        
        
    
    global cnt
    res = []
    for i in range(len(queryType)):
        if queryType[i] == 'Total':
            cnt=0
            visited = [False] * (n+1)
            dfs(graph,students1[i],visited)
            if visited[students2[i]]==False:
                dfs(graph,students2[i],visited)
            res.append(str(cnt))
            
        elif queryType[i] == 'Friend':
            graph[students1[i]].append(students2[i])
            graph[students2[i]].append(students1[i])
        
    return res