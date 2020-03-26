import itertools


city = open('./cities.html', 'r')
mcity = city.read()


def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

word = input('enter the list of characters \n')
perms = list(itertools.permutations(word))

for perm in perms:
    newWord = listToString(perm)
    if newWord in mcity:
        print(newWord)
        break

