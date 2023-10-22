def sumpowers(n, p):
    sum = 0
    for i in range(1, n+1):
        sum += i**p
    return sum


print(sumpowers(10, 2))

def terms(big, p):
    sum = 0
    n = 0
    while sum < big:
        n += 1
        sum += n**p
    return n


print(terms(10, 2))

