# import timeit
import math


# Write a Python program to create a dictionary from a string and track the count of the letters from the string.
# Sample string : “Marmignon”
# Expected output: {'M': 1, 'a': 1, 'r': 1, 'm': 1, 'i': 1, 'g': 1, 'n': 2, 'o': 1}


def exam1(string_to_count='Marmignon'):
    """
    Counts number of occurrences of every letter of a string.
    :param string_to_count: String from which to count.
    :return: Dictionary of letters and their count.
    """
    dictionary_of_letters = {}
    for letter in string_to_count:
        if letter in dictionary_of_letters:
            dictionary_of_letters[letter] += 1
        else:
            dictionary_of_letters[letter] = 1
    return dictionary_of_letters


# How would you switch the values of two integer variables without using a third variable?
def exam2(a=111, b=222):
    """
    Interchanges the values of two given variables.
    :param a: First variable (default 111).
    :param b: Second variable (default 222).
    :return: a, b
    """
    print('BEFORE : a = {} ; b = {}'.format(a, b))
    a, b = b, a
    print('AFTER : a = {} ; b = {}'.format(a, b))
    return a, b


# Write a Python Program to Check if a Number is a Palindrome or not
def exam3(number=12321):
    """
    Checks whether given number is a palindrome.
    :param number: Number to check (default 12321).
    :return: True if number is a palindrome, false if it is not.
    """
    number = str(number)
    for n in range(len(number) // 2):
        if number[n] != number[-n - 1]:
            return False
    return True


# Write a Python Program to Check if a Number is a Prime Number.
def exam4(number=7919):
    """
    Checks whether given number is prime.
    :param number: Number to check (default 7919).
    :return: True if number is prime, false if it is not.
    """
    if number < 2:
        return False
    if number == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True


# Write a Python Program to Find the Second-Largest Number in a List
def exam5(list_to_sort=[12, 322, 14323, 8766544, 77777]):
    """
    Finds the second-largest element in a given list. Will raise IndexError if insufficient number of elements.
    :param list_to_sort: List of elements given.
    :return: Second-largest element.
    """
    sorted_list = list_to_sort.copy()
    sorted_list.sort()
    return sorted_list[-2]


# Theoretically more optimized, but less python-oriented alternative
def exam5_2(list_to_sort=[12, 322, 14323, 8766544, 77777]):
    """
    Finds the second-largest element in a given list. Will raise IndexError if insufficient number of elements.
    :param list_to_sort: List of elements given.
    :return: Second-largest element.
    """
    largest = float('-inf')
    second_largest = float('-inf')
    for element in list_to_sort:
        if largest <= element:
            second_largest, largest = largest, element
        elif second_largest <= element:
            second_largest = element
    if second_largest == float('-inf'):
        raise IndexError
    return second_largest


if __name__ == '__main__':

    _var_exam1 = 'Marmignon'
    _var_exam2 = (111, 222)
    _var_exam3 = 12321
    _var_exam4 = 7919
    _var_exam5 = [12, 322, 14323, 8766544, 77777]
    _var_exam5_2 = [12, 322, 14323, 8766544, 77777]

    # # Test validity of exam4() with known results
    # _var_test_exam4 = [i for i in range(1000) if exam4(i)]
    # _var_test_exam4_solution = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
    #                             61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
    #                             131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193,
    #                             197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269,
    #                             271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
    #                             353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431,
    #                             433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503,
    #                             509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
    #                             601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673,
    #                             677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761,
    #                             769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857,
    #                             859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947,
    #                             953, 967, 971, 977, 983, 991, 997]
    # assert _var_test_exam4 == _var_test_exam4_solution

    print(f'The count of letters in {_var_exam1} is {exam1(_var_exam1)}')
    exam2(*_var_exam2)
    print(f'"{_var_exam3}" is a palindrome.' if exam3(_var_exam3) else f'"{_var_exam3}" is not a palindrome.')
    print(f'"{_var_exam4}" is prime.' if exam4(_var_exam4) else f'"{_var_exam4}" is not prime.')
    print(f'The second-largest element in the list "{_var_exam5}" is "{exam5(_var_exam5)}"')
    print(f'The second-largest element in the list "{_var_exam5_2}" is "{exam5_2(_var_exam5_2)}"')
    # print(timeit.timeit("exam5([i for i in range(5555)][::-1])", number=10000, globals={'exam5': exam5}))
    # print(timeit.timeit("exam5_2([i for i in range(5555)][::-1])", number=10000, globals={'exam5_2': exam5_2}))
