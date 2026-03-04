words = ['hello', 'WORLD', 'Python', 'java', 'AI']

transformed_words = []

for word in words:
    if word.islower():
        transformed_words.append(word.upper())

    elif word.isupper():
        transformed_words.append(word.lower())

    else:
        transformed_words.append(word)

print(transformed_words)