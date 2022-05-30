# o(n**2)
def bubble_sort(arr):

    n = len(arr)

    for i in range(n):
        for j in range(i, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr



if __name__ == '__main__':

    arr = list(range(20))

    from random import shuffle
    shuffle(arr)

    print(arr)
    print(bubble_sort(arr))


