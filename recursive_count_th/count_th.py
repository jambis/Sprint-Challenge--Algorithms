'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    total = 0

    if len(word) < 2:
        print(word)
        return total

    elif word[:2] == "th":
        print("elif ran")
        total = 1 + count_th(word[2:])

    else:
        print("else ran")
        total = count_th(word[1:])

    return total


word = "athcabc"
# print(word[:2])

print(count_th(word))
