# Author @tiggreen

def merge_sort(lst):
    """ sort the given list with merge sort. nlog(n)"""
    if len(lst) <= 1:
        return lst

    (half1, half2) = split(lst)
    return merge(merge_sort(half1), merge_sort(half2))


def split(lst):
    evens = []
    odds = []
    is_even = True
    for e in lst:
        if is_even:
            evens.append(e)
        else:
            odds.append(e)
        is_even = not is_even

    return (evens, odds)


def merge(sorted1, sorted2):
    result = []
    index1 = 0
    index2 = 0
    while index1 < len(sorted1) and index2 < len(sorted2):
        if ( sorted1[index1] <= sorted2[index2]):
            result.append(sorted1[index1])
            index1 = index1 + 1
        else:
            result.append(sorted2[index2])
            index2 = index2 + 1

    if index1 < len(sorted1):
        result.extend(sorted1[index1:])
    elif index2 < len(sorted2):
        result.extend(sorted2[index2:])

    return result


def quick_sort(lst):
    """ sort the given list quick sort. nlog(n)"""
    if not lst:
        return lst
    # take the first element as a pivot
    pivot = lst[0]
    (less, same, more) = partition(pivot, lst)
    return quick_sort(less) + same + quick_sort(more)


def partition(pivot, lst):
    (less, same, more) = ([], [], [])
    for e in lst:
        if e < pivot:
            less.append(e)
        elif e > pivot:
            more.append(e)
        else:
            same.append(e)
    return (less, same, more)


def main():
    a = [1, 5, 55, 7, 10, 8, 0, 3, 1, 2, 2, 12, 33, 18]
    b = [1, 6, 3, 4, 12, 55, 33, 33, 44, 17, 16]
    print ("Quick Sort result: " + str(quick_sort(a)))
    print ("Merge Sort result: " + str(merge_sort(b)))

if __name__ == '__main__':
    main()
