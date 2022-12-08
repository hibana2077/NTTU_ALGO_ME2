import sys
ans = sys.maxsize
s1 = s2 = str()
start = tar = [0,0]
mov = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
dp = [[0 for _ in range(9)] for _ in range(9)]
f1 = lambda x,y: 0 < x < 9 and 0 < y < 9

def init():
    global start, tar
    start = [ord(s1[0]) - ord('a') + 1, ord(s1[1]) - ord('0')]
    tar = [ord(s2[0]) - ord('a') + 1, ord(s2[1]) - ord('0')]
    for i in range(1, 9):
        for j in range(1, 9):
            dp[i][j] = ans

def DFS(now:list,cnt=0):
    global dp,ans,tar,mov
    if cnt>dp[now[0]][now[1]] or cnt > dp[tar[0]][tar[1]]:return
    dp[now[0]][now[1]] = cnt
    if now == tar:return
    nxt = [0,0]
    for t in mov:
        nxt[0] = now[0] + t[0]
        nxt[1] = now[1] + t[1]
        if f1(nxt[0],nxt[1]):
            DFS(nxt,cnt+1)

def main():
    global s1,s2,ans
    for _ in range(int(input())):
        s1, s2 = input().split()
        init()
        DFS(start)
        print(dp[tar[0]][tar[1]])

if __name__ == '__main__':main()