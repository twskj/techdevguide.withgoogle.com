# Given a non-empty array, return true if there is a place to split the array
# so that the sum of the numbers on one side is equal to
# the sum of the numbers on the other side.


# canBalance([1, 1, 1, 2, 1]) → true
# canBalance([2, 1, 1, 2, 1]) → false
# canBalance([10, 10]) → true


def canBalance(arr):

    half = sum(arr) / 2

    sumSoFar = 0
    i = 0
    while sumSoFar <= half:

        if sumSoFar == half:
            return True

        sumSoFar += arr[i]
        i += 1
    
    return False

print(canBalance([1, 1, 1, 2, 1]))
print(canBalance([2, 1, 1, 2, 1]))
print(canBalance([10, 10]))
