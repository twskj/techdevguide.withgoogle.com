# Given a string, return the sum of the numbers appearing in the string
# , ignoring all other characters. A number is a series of 1 or more digit chars in a row.
# (Note: Character.isDigit(char) tests if a char is one of the chars '0', '1', .. '9'.
# Integer.parseInt(string) converts a string to an int.)


# sumNumbers("abc123xyz") → 123
# sumNumbers("aa11b33") → 44
# sumNumbers("7 11") → 18

def sumNumbers(str):

    i = 0
    totalSum = 0
    tmp = ""
    nums = set(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
    while i < len(str):

        ch = str[i]
        if ch in nums:
            tmp += ch
        elif tmp != "":
            totalSum += int(tmp)
            tmp = ""
        i += 1
    if tmp != "":
        totalSum += int(tmp)
    return totalSum


print(sumNumbers("abc123xyz"))
print(sumNumbers("aa11b33"))
print(sumNumbers("7 11"))
