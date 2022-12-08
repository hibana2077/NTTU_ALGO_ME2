

for _ in range(int(input())):
    cook_time_and_eat_time = [list(map(int, input().split())) for _ in range(int(input()))]
    jaylan = cook_time_and_eat_time[0]
    cook_time_and_eat_time = sorted(cook_time_and_eat_time, key=lambda x: x[1],reverse=True)
    jaylan_loc=tt=rt= 0
    for i in range(0, len(cook_time_and_eat_time)):
        if jaylan == cook_time_and_eat_time[i]:jaylan_loc = i
    for i in range(0, len(cook_time_and_eat_time)):
        rt+=cook_time_and_eat_time[i][0]
        tt=max(rt+cook_time_and_eat_time[i][1],tt)
    print(f"{tt},{jaylan_loc+1}")