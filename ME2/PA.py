
#Jolly Jumpers

while True:
    try:
        a = list(map(int, input().split()))
        n = a[0]
        a.pop(0)
        if n == 0:
            break
        else:
            b = [abs(a[i] - a[i+1]) for i in range(n-1)]
            if sorted(b) == list(range(1, n)):
                print("Jumping Number")
            else:
                print("Not Jumping Number")
    except EOFError:
        break