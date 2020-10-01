from numpy.random import seed
from numpy.random import randint

seed(1)

values = randint(0,2000000000,20000000)


arr = [54, 26, 93, 17, 77, 31, 44, 55, 20, 88]


def MergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        MergeSort(left)
        MergeSort(right)

        # left and right array traversal var i and j

        i = 0
        j = 0

        # main array manipulating var k

        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i = i + 1
            else:
                arr[k] = right[j]
                j = j + 1
            k = k + 1
        while i < len(left):
            arr[k] = left[i]
            i = i + 1
            k = k + 1
        while j < len(right):
            arr[k] = right[j]
            j = j + 1
            k = k + 1


MergeSort(values)
print(values)
