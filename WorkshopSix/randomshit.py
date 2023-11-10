punctuation = '!"#$%&`()*+,-./:;'
lines = 'this is a -(, string with too much /= punctuation!'
for s in punctuation:
    lines = lines.replace(s, " ")

word_freq = {}
for line in lines:
    for p in punctuation:
        line = line.replace(p, '')
    words = line.split(' ')
    for word in words:
        word = word.strip().lower()
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

print(word_freq)