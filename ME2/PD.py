
def cacu_step(start,end):
    dp = [-1 for _ in range(200001)]
    pos_queue = [start]
    dp[start] = 0
    while True:
        if  pos_queue[0]-1 >= 0 and dp[pos_queue[0]-1] == -1:
            pos_queue.append(pos_queue[0]-1)
            dp[pos_queue[0]-1] = dp[pos_queue[0]] + 1
        if pos_queue[0]+1 <= 200000 and dp[pos_queue[0]+1] == -1:
            pos_queue.append(pos_queue[0]+1)
            dp[pos_queue[0]+1] = dp[pos_queue[0]] + 1
        if pos_queue[0]*2 <= 200000 and dp[pos_queue[0]*2] == -1:
            pos_queue.append(pos_queue[0]*2)
            dp[pos_queue[0]*2] = dp[pos_queue[0]] + 1
        if dp[end] != -1:return dp[end]
        pos_queue.pop(0)

for _ in range(int(input())):
    a,b = map(int,input().split())
    if a==b:print(0)
    else:
        print(cacu_step(a,b))
