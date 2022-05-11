#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
def match_words(words):
    count = 0
    for word in words:
        print(word)
        if len(word) > 1 and word[0] == word[-1]:
            count = count + 1
    return count

print(match_words(['abc', 'xyz', 'aba', '1221']))