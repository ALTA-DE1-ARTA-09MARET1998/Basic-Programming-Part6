def find_max_sum_sub_array(k, arr):
    listmax = 0
    for i in range(len(arr) - 1):
        sum = arr[i] + arr[i + 1]
        if sum > listmax:
            listmax = sum
        print(listmax)
            
    # for number in arr:
    #     if number > min(arr):
    #         listmax.append(number)
    # maxnum = sum(listmax)

    # result = []
    #     for j in range (i, len(arr)):
    #         k += arr [j]
    #         if k > result[0]:
    #             result.insert(0, k) 

    # if k == arr[-1]:
    #     for i in range(len(arr) -1):
    #         if arr[-2] + arr[i] == k:
    #             result.append(i)
    #             result.append(len(arr) -2)
    # else:
    #     for i in range(len(arr) -1):
    #         if arr[i] + arr[i + 1] == k:
    #             result.append(i)
    #             result.append(i + 1)
    # return result

    #     for j in range(arr.index(i) + 1, len(arr)):
    #         i += arr[j]
    #         sums.append(i)
    # if all(j < 0 for j in arr) or not sums:
    #     return 0
    # else:
    #     max_sum = max(sums)
    #     return max_sum




if __name__ == '__main__':
    print(find_max_sum_sub_array(3, [2, 1, 5, 1, 3, 2])) # 9
    print(find_max_sum_sub_array(2, [2, 3, 4, 1, 5])) # 7
    print(find_max_sum_sub_array(2, [2, 1, 4, 1, 1])) # 5
    print(find_max_sum_sub_array(3, [2, 1, 4, 1, 1])) # 7
    print(find_max_sum_sub_array(4, [2, 1, 4, 1, 1])) # 8