def set_method(arr, cmd, cmd_set):
    if cmd == 'update':
        arr.update(cmd_set)
    elif cmd == 'intersection_update':
        arr.intersection_update(cmd_set)
    elif cmd == 'symmetric_difference_update':
        arr.symmetric_difference_update(cmd_set)
    elif cmd == 'difference_update':
        arr.difference_update(cmd_set)
    else:
        print('error')

    return arr


init_num = int(input())
init_set = set(map(int, input().split()))
work_cycle = int(input())
arr = init_set

for a in range(0, work_cycle):
    cmd_arr = input().split()
    cmd = cmd_arr[0]
    num = int(cmd_arr[1])
    cmd_set = set(map(int, input().split()))
    arr = set_method(arr, cmd, cmd_set)

print(sum(arr))
