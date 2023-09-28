def find_max_sum_sub_array(k, arr):
    
    # if k <= 0 or k > len(arr):
    #         return None
    
    # highest_sum = float('-inf')
    # sums = sum(arr[:k])

    for i in range(k, len(arr)):
        sums += arr[i] - arr [i - k]
        highest_sum = max(highest_sum, sums)

        return highest_sum

if __name__ == '__main__':
    print(find_max_sum_sub_array(3, [2, 1, 5, 1, 3, 2])) # 9
    print(find_max_sum_sub_array(2, [2, 3, 4, 1, 5])) # 7
    print(find_max_sum_sub_array(2, [2, 1, 4, 1, 1])) # 5
    print(find_max_sum_sub_array(3, [2, 1, 4, 1, 1])) # 7
    print(find_max_sum_sub_array(4, [2, 1, 4, 1, 1])) # 8