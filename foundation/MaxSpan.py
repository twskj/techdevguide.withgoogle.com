# Consider the leftmost and righmost appearances of some value in an array.
# We'll say that the "span" is the number of elements between the two inclusive.
# A single value has a span of 1. Returns the largest span found in the given array.
# (Efficiency is not a priority.)

# maxSpan([1, 2, 1, 1, 3]) → 4
# maxSpan([1, 4, 2, 1, 4, 1, 4]) → 6
# maxSpan([1, 4, 2, 1, 4, 4, 4]) → 6


def maxSpan(arr,count=0):
    
    reverse_idx = {}

    for i in range(len(arr)):
        item = arr[i]
        if item not in reverse_idx:
            reverse_idx[item] = []
        reverse_idx[item].append(i)

    maxSpan = 0
    for key in reverse_idx:
        diff = max(reverse_idx[key]) - min(reverse_idx[key]) + 1
        if diff > maxSpan:
            maxSpan = diff
    
    return maxSpan
        

print(maxSpan([1, 2, 1, 1, 3]) == 4)
print(maxSpan([1, 4, 2, 1, 4, 1, 4]) == 6)
print(maxSpan([1, 4, 2, 1, 4, 4, 4]) == 6)
