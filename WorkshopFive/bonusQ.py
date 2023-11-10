def square_numbers(N):
    i = 0
    while True:
        sq = i * i
        if sq > N:
            break
        yield sq
        i = i + 1


for value in square_numbers(1000000):
    print(value)

# Write your own generator function that iterates on each letter
# in a string and creates a shift cypher with index 1
# printing each letter as it goes. The ord() and chr()
# functions will help access and increment the ascii value of the letter.

letter = 'a'
cypher_text = chr(ord(letter) + 1)