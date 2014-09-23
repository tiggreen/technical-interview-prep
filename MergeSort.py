"""
author @tiggreen 

Sorting is cool! So let's do it. 
Divide-and-conquer sorting algorithm.

"""


def quickSort(lst):
    if not lst:
        return lst
    # let's get the pivot first
    pivot = lst[len(lst) // 2]
    # let's now partition the list based on the pivot
    (less, same, more) = partition(lst, pivot)
    return quickSort(less) + same + quickSort(more)


def partition(lst, pivot):
    less = []
    more = []
    same = []
    for i in lst:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            more.append(i)
        else:
            same.append(i)
    return (less, same, more)


def mergeSort(lst):
    if not lst:
        return lst
    elif len(lst) == 1:
        return lst
    else:
        (lst1, lst2) = split(lst)
        return merge(mergeSort(lst2), mergeSort(lst2))


# splits the list into even and odd indexed numbers
# eg. (1,5,6,6,7,12) => (1,6,7), (5,6,12)
def split(lst):
    evens = []
    odds = []
    isEven = True
    for i in lst:
        if isEven:
            evens.append(lst[i])
        else:
            odds.append(lst[i])
        isEven = not isEven
    return (evens, odds)


#merges two lists into one sorted list.
def merge(sorted1, sorted2):
    result = []
    pass


def main():
    lst = [1, 10, 3, 5, 8, 4, 23, 19, 2, 1]
    print(quickSort(lst))


main()