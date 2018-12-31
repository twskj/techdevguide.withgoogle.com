# Given two strings, base and remove, return a version of the base string where
# all instances of the remove string have been removed (not case sensitive).
# You may assume that the remove string is length 1 or more.
# Remove only non-overlapping instances, so with "xxx" removing "xx" leaves "x".

# withoutString("Hello there", "llo") → "He there"
# withoutString("Hello there", "e") → "Hllo thr"
# withoutString("Hello there", "x") → "Hello there"


def match(src, target, idx):

    for i in range(len(target)):
        if target[i] != src[i+idx]:
            return False
    return True


# O(n*m)
def withoutString(source, target):

    result = ""
    i = 0
    while i < len(source):
        if source[i] == target[0] and match(source, target, i):
            i += len(target) - 1
        else:
            result += source[i]
        i += 1

    return result


print(withoutString("Hello there", "llo"))
print(withoutString("Hello there", "e"))
print(withoutString("Hello there", "x"))
