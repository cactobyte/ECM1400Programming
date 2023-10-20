def isOdd(num):
    if num % 2 == 1:
        return True


def odd_even(L):
    odd_sum, even_sum = 0, 0
    """Complete the function logic and update this docstring"""
    for each_number in L:
        if type(each_number) == int or type(each_number) == float:
            if isOdd(each_number) == True:
                odd_sum += each_number
            else:
                even_sum += each_number
    return odd_sum, even_sum


L = [1, 42, -3, 2.4, 'invalid input']
odd_sum, even_sum = odd_even(L)
print(odd_sum, even_sum)
