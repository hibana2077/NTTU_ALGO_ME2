
def binary_search_count_step(data : list, target: int) -> int:
    step = 0
    left, right = 0, len(data) - 1
    while left <= right:
        step += 1
        mid = (left + right) // 2
        if data[mid] == target:
            return step
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return step


while True:
    try:
        list_in = list(map(int,input().split(" ")))
        num = int(input())
        print(binary_search_count_step(list_in, num)-1) if num in list_in else print(-1)
    except EOFError:
        break