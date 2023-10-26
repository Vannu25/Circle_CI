# Write a Python script to implement the Bubble sort algorithm.
import array


def bubble_Sort(arr):
    n = len(arr)  # length would be 7

    for i in range(n - 1):  # 0, 1, 2, 3, 4, 5
        # print(i)

        for j in range(0, n - i - 1):  # continuous of above outcome
            print(j)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(arr)


# example arr
arr = [23, 14, 64, 13, 64, 23, 86]

bubble_Sort(arr)
