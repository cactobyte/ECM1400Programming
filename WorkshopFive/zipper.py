def zipper(a, b):
    out = []
    for i in range((len(a))):
        out.append([a[i], b[i]])
    return out


print(zipper ([3 , 4 , 5 , 6] , ["a", "b", "c", "d"]))
