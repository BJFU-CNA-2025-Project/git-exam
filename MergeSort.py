def merge(array, l, mid, r):
    tmpl = array[l:mid+1]
    tmpr = array[mid+1:r+1]

    i = 0
    j = 0
    k = l
    while i < len(tmpl) and j < len(tmpr):
        if tmpl[i] <= tmpr[j]:
            array[k] = tmpl[i]
            k += 1
            i += 1
        else:
            array[k] = tmpr[j]
            k += 1
            j += 1

    while i < len(tmpl):
        array[k] = tmpl[i]
        k += 1
        i += 1

    while j < len(tmpr):
        array[k] = tmpr[j]
        k += 1
        j += 1


def merge_sort(array, l, r):
    if l < r:
        mid = (l + r) // 2
        merge_sort(array, l, mid)
        merge_sort(array, mid + 1, r)
        merge(array, l, mid, r)

def main():

    array = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]

    print(array)

    merge_sort(array, 0, len(array) - 1)

    print(array)

if __name__ == '__main__':
    main()


