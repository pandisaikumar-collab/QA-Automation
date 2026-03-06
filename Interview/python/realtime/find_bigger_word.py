input_str = "python is good programming language"

big_word = " "

for word in input_str.split():
    if len(word) >len(big_word):
        big_word = word

print(big_word)