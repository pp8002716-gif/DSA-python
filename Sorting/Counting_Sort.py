def counting_sort(arr):
    if not arr:
        return arr

    max_value = max(arr)
    min_value = min(arr)

    count = [0] * (max_value - min_value + 1)

    for num in arr:
        count[num - min_value] += 1

    index = 0

    for i in range(len(count)):
        while count[i] > 0:
            arr[index] = i + min_value
            index += 1
            count[i] -= 1

    return arr


arr = list(map(int, input("Enter numbers: ").split()))

print("Sorted array:", counting_sort(arr))