def time_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

def tim_sort(arr):
    min_run = 32
    n = len(arr)

    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)

    size = min_run
    while size < n:
        for left in range(0, n, size * 2):
            mid = min(n - 1, left + size - 1)
            right = min((left + size * 2 - 1), (n - 1))
            if mid < right:
                merge(arr, left, mid, right)
        size *= 2

my_list = [56, 64, 32, 45, 12, 2, 5, 65]

print("Список до сортировки:", my_list)
tim_sort(my_list)
print("Список после сортировки:", my_list)


def selection_sort(arr):
    sorted_arr = arr[:]
    n = len(sorted_arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if sorted_arr[j] < sorted_arr[min_idx]:
                min_idx = j
        sorted_arr[i], sorted_arr[min_idx] = sorted_arr[min_idx], sorted_arr[i]
    return sorted_arr



print("До сортировки:", my_list)
sorted_numbers = selection_sort(my_list)
print("После сортировки:", sorted_numbers)



def bubble_sort(arr):
    sorted_arr = arr[:]
    n = len(sorted_arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if sorted_arr[j] > sorted_arr[j+1]:
                sorted_arr[j], sorted_arr[j+1] = sorted_arr[j+1], sorted_arr[j]
    return sorted_arr


print("До сортировки:", my_list)
sorted_numbers = bubble_sort(my_list)
print("После сортировки:", sorted_numbers)
