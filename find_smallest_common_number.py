# Given three integer arrays sorted in ascending order, find the smallest number
# that is common in all three arrays.

def find_smallest(a, b, c):

    i = 0 # a pointer
    j = 0 # b pointer
    k = 0 # c pointer

    # how to iterate through largest list?
    while (i < len(a)) and (j < len(b)) and (k < len(c)):

        if (a[i] == b[j]) and (a[i] == c[k]):
            return a[i]

        if (a[i] <= b[j]) and (a[i] <= c[k]):
            i += 1
        elif (b[j] <= a[i]) and (b[j] <= c[k]):
            j += 1
        elif (c[k] <= a[i]) and (c[k] <= b[j]):
            k += 1

    return -1

a = [7, 10, 25, 30, 50, 63, 64]
b = [-1, 4, 5, 6, 7, 8, 50]
c = [1, 10, 14, 50, 60]

print(find_smallest(a, b, c))
