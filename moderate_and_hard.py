# @tiggreen
# Some random moderate and hard problems.

def decimal_to_binary(n):
    """
    Converts the decimal (10 based) number to a binary number
    decimal_to_binary(8) => 1000
    """
    binary_list = []
    while n > 1:
        if n % 2 == 0:
            binary_list.insert(0,0)
        else:
            binary_list.insert(0,1)
        n = n // 2

    binary_list.insert(0,1)
    return binary_list


def reverse_words_in_place(str):
    if len(str.split()) == 1:
        return str
    return str.split()[-1] + " " + reverseWordsInPlace(' '.join(str.split()[:-1]))


# [1, 2, 3], [4, 5, 6, 7] ==> [1, 2, 3, 4, 5, 6, 7]
def merge_sorted_lists(lst1,lst2):
    #let's check if one of them is empty
    if not lst1:
         return lst2
    if not lst2:
         return lst1

    i = 0
    j = 0
    # idealy we want to have len(lst1) + len(lst2) size list
    sorted_merged_list = []
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            sorted_merged_list.append(lst1[i])
            i+=1
        else:
            sorted_merged_list.append(lst2[j])
            j+=1

    # there might be some leftover elements in lists so let's
    # check it out.
    while i < len(lst1):
        sorted_merged_list.append(lst1[i])
        i+=1
    while j < len(lst2):
        sorted_merged_list.append(lst2[j])
        j+=1

    return sorted_merged_list

def binary_search_recursive(lst, data):
    if not lst:
        return False

    mid_index = len(lst) // 2

    if lst[mid_index] == data:
        return True
    if data < lst[mid_index]:
        return binary_search_recursive(lst[:mid_index], data)
    elif data > lst[mid_index]:
        return binary_search_recursive(lst[mid_index+1:], data)


def get_all_permutations(st):
    """
    Return all the permutations of the string.
    E.g. "abc" => "abc", "acb", "bac", "bca", "cab", "cba" 
    """
    perms = []
    if st is None:
        return st
    # the base case.
    if len(st) == 0:
        perms.append('')
        return perms
    else:
        first = st[0]
        remainder = st[1:]

        words = get_all_permutations(remainder)
        for w in words:
            for i in range(len(w)+1):
                perms.append(insert_char_at(w,first,i))
        return perms

def insert_char_at(st, f, pos):
    result = st[:pos] + f + st[pos:]
    return result

# ls = [a,b] => [[], a, b, [a,b]]
def get_power_set(ls):
    all_subsets = []
    sz = 1 << len(ls)
    for counter in range(sz):
        temp_subset  = []
        for j in range(len(ls)):
            if (counter & 1 << j) > 0:
                temp_subset.append(ls[j])
        all_subsets.append(temp_subset)
    return all_subsets


def get_power_set_better(lst):
    if s == []:
        return [[]]

    first = s[0]
    remainder = s[1:]
    q = get_power_set_better(remainder)

    return q + [x + [first] for x in q]


def find_pair_sum(lst, sm):
    """
    Finding pair of numbers in a list that add to given sum.
    a = [1,3,4,6,12,16,19, 10]
    findPairSum(a, 28) => (12,16)
    key : sum - x, value y
    """
    if not lst:
        return lst
    d = dict()
    result = []
    for i in lst:
        if i not in d:
            d[sm - i] = i
        else:
            key = sm - i
            result.append((key,i))

    return result


def print_all_parens(cnt):
    """Print all valid combinations of n-pairs of parentheses."""
    st = ['' for i in range(cnt*2)]
    return print_all_parens_util(cnt, cnt, 0, st)

def print_all_parens_util(left, right, cnt, st):
    if left < 0 or left > right:
        return

    if left == 0 and right == 0:
        print(st)
    else:
        if left > 0:
            st[cnt] = '('
            print_all_parens_util(left-1, right, cnt+1, st)
        if right > left:
            st[cnt] = ')'
            print_all_parens_util(left, right-1, cnt+1, st)


def pow(x,n):
    """ calculate x raised to the power n """
    if n == 0:
        return 1
    elif n % 2 == 0:
        return pow(x, n//2)*pow(x, n//2)
    else:
        return x*pow(x, n//2)*pow(x, n//2)


def word_break(st, dic):
    """
    Given an input string and a dictionary of words, find out if
    the input string can be segmented into a space-separated sequence of 
    dictionary words. See following examples for more details.
    """
    #base case
    if len(st) == 0:
        return True
    for i in range(1,len(st) + 1):
        if st[0:i] in dic and word_break(st[i:len(st)-i], dic):
            return True
    return False


def remove_duplicate_chars_from_string(st):
    """
    "abcdbfa" => "cdbfa" (do this in place)
    Q: Do we want to remove first occurance chars or the second, or next?
    """
    if st == None:
        return None

    # let this be the base case
    if st == "":
        return st

    head = st[0]
    tail = st[1:]
    if head in tail:
        return remove_duplicate_chars_from_string(tail)
    else:
        return head + remove_duplicate_chars_from_string(tail)


def reverse_string(st):
    if st is None:
        return None
    if st == "":
        return st
    return st[-1] + reverse_string(st[:-1])


def reverse_digits(num):
    """
    Reverse the digits of an integer
    12345 -> 54321
    """
    newnum  = 0
    while num > 0:
        digit = num % 10
        num = num // 10
        newnum = newnum*10 + digit
    return newnum       

def main():
    print(reverse_digits(1))

if __name__ == '__main__':
    main()