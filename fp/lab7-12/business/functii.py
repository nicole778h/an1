def find_id(lista):
    id = 0
    id = str(id)
    lista_ids = [x.get_id() for x in lista]
    while id in lista_ids:
        id = int(id)
        id += 1
        id = str(id)
    return id


def mergesort(sir, key=lambda el: el, reverse=False):
    lista = []
    comp = lambda a, b: a <= b
    if reverse == True:
        comp = lambda a, b: a >= b
    for x in sir:
        lista.append(x)
    mergeSort_sort(lista, 0, len(sir) - 1, key, comp)
    return lista


# Python program for implementation of MergeSort

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]


def merge(arr, l, m, r, key, comp):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if comp(key(L[i]), key(R[j])):
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort_sort(arr, l, r, key, comp):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        mergeSort_sort(arr, l, m, key, comp)
        mergeSort_sort(arr, m + 1, r, key, comp)
        merge(arr, l, m, r, key, comp)


# Function to print the Array
def printArray(arr):
    print("Sorted Array: ", end="")
    for ele in arr:
        print(ele, end=" ")
    print()


# function for Sorting the Array
def bingosort_sort(arr, size, key, comp):
    # Finding the smallest element From the Array
    bingo = min(arr, key=lambda el: key(el))

    # Finding the largest element from the Array
    largest = max(arr, key=lambda el: key(el))
    nextBingo = largest
    nextPos = 0
    while key(bingo) < key(nextBingo):

        # Will keep the track of the element position to
        # shifted to their correct position
        startPos = nextPos
        for i in range(startPos, size):
            if key(arr[i]) == key(bingo):
                arr[i], arr[nextPos] = arr[nextPos], arr[i]
                nextPos += 1

            #  Here we are finding the next Bingo Element
            #  for the next pass
            elif comp(key(arr[i]), key(nextBingo)):
                nextBingo = arr[i]
        bingo = nextBingo
        nextBingo = largest


def bingosort(sir, key=lambda el: el, reverse=False):
    lista = []
    comp = lambda a, b: a <= b
    if reverse == True:
        comp = lambda a, b: a >= b
    for x in sir:
        lista.append(x)
    bingosort_sort(lista, len(lista), key, comp)
    return lista
