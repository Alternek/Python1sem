arr = [int(i) for i in input().split()]
k = 1
k_arr = [arr[0]]
ans = 0
ans_arr = []
for i in range(1, len(arr)):
    if arr[i] > arr[i - 1]:
        k += 1
        k_arr.append(arr[i])
    else:
        if k > ans:
            ans = k
            ans_arr = k_arr.copy()
        k = 1
        k_arr = [arr[i]]
if k > ans:
    ans = k
    ans_arr = k_arr.copy()
print(*ans_arr)
