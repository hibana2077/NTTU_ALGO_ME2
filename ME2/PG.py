
from functools import cmp_to_key
class Node:
    def __init__(self,x,y,dis,freq):
        self.x = x
        self.y = y
        self.dis = dis
        self.freq = freq

def cmp(a:Node,b:Node):
    return  a.freq > b.freq if a.freq!=b.freq else a.dis < b.dis
    
while True:
    try:
        m,n,city = map(int,input().split())
        if n==m==city==0:break
        graph = list()
        vist = [False for _ in range(n+1)]
        for _ in range(n):
            temp = list(map(int,input().split()))
            graph.append(Node(temp[0],temp[1],temp[2],temp[3]))
        graph = sorted(graph,key=cmp_to_key(cmp))

        vist[city] = True
        print(city,end=' ')
        while n>0:
            for t in range(m):
                if vist[graph[t].x]+vist[graph[t].y]==1:
                    if vist[graph[t].x]:
                        print(graph[t].y,end=' ')
                        vist[graph[t].y] = True
                    else:
                        print(graph[t].x,end=' ')
                        vist[graph[t].x] = True
                    break
            n-=1
        print()
    except EOFError:break