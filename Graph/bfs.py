from collections import deque

def bfs(graph,start,end):
    queue = deque()
    queue.appendleft(start)
    while queue:
        vertex = queue.pop()
        if visited[vertex]: continue
        if vertex == end:
            return True 
        visited[vertex] = True 
        for node in graph[vertex]:
            if visited[node]: continue
            queue.appendleft(node)
            prev[node] = vertex


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
    hashpath = bfs(graph,start,end)
    print(hashpath)
    print(prev)
