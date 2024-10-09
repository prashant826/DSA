from collections import deque
def dfs(start,graph):

    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex in visited: continue
        print(vertex,end = " ")
        visited.add(vertex)
        for node in graph[vertex]:
            if node not in visited:
                stack.append(node)

if __name__ == '__main__':
    n,k = map(int,input().split())
    graph = dict()
    visited = [0]*(n+1) 
    prev = [0]*(n+1)
    for i in range(1,n+1):
        graph[i] = set()

    for i in range(k):
        a,b = map(int,input().split())
        graph[a].add(b)
        # if un-directed
        #graph[b].add(a)
    start,end = map(int,input().split())
    dfs(graph,start,end)