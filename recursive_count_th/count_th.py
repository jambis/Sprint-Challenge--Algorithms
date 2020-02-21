'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    total = 0

    if len(word) < 2:
        return total

    elif word[:2] == "th":
        total = 1 + count_th(word[2:])

    else:
        total = count_th(word[1:])

    return total
