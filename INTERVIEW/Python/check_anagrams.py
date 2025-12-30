# anagrams: check if two strings are same frequency of characters
# regardless of order

def check_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if check_anagrams(s1, s2):
    print("It is an anagram.")
else:
    print("It is not an anagram.")

