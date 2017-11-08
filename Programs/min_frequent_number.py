arr_list = list(map(int, input().split()))

n = len(arr_list)
for i in range(n):
    arr_list[arr_list[i]%n]+=n

# For max frequent
# print(arr_list.index(max(arr_list)))

print(arr_list.index(min(arr_list)))
