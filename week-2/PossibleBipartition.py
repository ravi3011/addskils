from collections import defaultdict

color = {}
graph = defaultdict(list)
def dfs(node,c = 0):
    if(node in color):
        return (color[node] == c)
    color[node] = c
    return all(dfs(i,c^1) for i in graph[node])


def check(n,dislike):
    
    for u,v in dislike:
        graph[u].append(v)
        graph[v].append(u)
    
    for node in range(1,n+1):
        if(node not in color):
            if(not dfs(node)):
                return False
    return True            

print(check(3,[[1,2],[1,3],[2,3]]))                    