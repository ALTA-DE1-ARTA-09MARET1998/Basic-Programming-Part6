def remove_duplicates(array):
    if len(array) == 0:
        return 0
    noduplicate = 0

    for i in range(1, len(array)):
        if array[i] != array[noduplicate]:
            noduplicate += 1
            array[noduplicate] = array[i]

    return noduplicate + 1

if __name__ == '__main__':
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9])) # 4
    print(remove_duplicates([2, 3, 4, 5, 6, 9, 9])) # 6
    print(remove_duplicates([2, 2, 2, 11])) # 2
    print(remove_duplicates([2, 2, 2, 11])) # 2
    print(remove_duplicates([1, 2, 3, 11, 11])) # 4