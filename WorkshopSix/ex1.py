def word_frequency(filename):
    word_count = {}
    punctuation = '!"#$%\&`()*+,-./:;>â€™!"#$%&Â´({})*+,-./:;<=>?@[]^_â€˜|~â€™'

    f = open(filename, "r")
    lines = [line.rstrip() for line in f.readlines()]
    for line in lines:
        for p in punctuation:
            line = line.replace(p, " ")
        words = line.lower().split()
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    return word_count


print(word_frequency("ex1.txt"))