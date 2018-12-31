# The Challenge
# Given a string S and a set of words D, find the longest word in D that is a subsequence of S.

# Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W,
# without reordering the remaining characters.

# Note: D can appear in any format (list, hash table, prefix tree, etc.

# For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"}
# the correct output would be "apple"

# The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
# The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right order.
# The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.
# Learning objectives
# This question gives you the chance to practice with algorithms and data structures.
# It’s also a good example of why careful analysis for Big-O performance is often worthwhile
# , as is careful exploration of common and worst-case input conditions.


class Solution(object):

    # O(m*n) m = number of word in word-bag; n = len of Main string
    def longestCommonSubSequence1(self, S, D):

        longestWord = ""
        for word in D:

            current = 0
            for s in S:
                if s == word[current]:
                    current += 1
                    if current > len(word) - 1:
                        break

            if current > len(word) - 1 and len(word) > len(longestWord):
                longestWord = word
        return longestWord

    # O(m*n) m = number of word in word-bag; n = len of Main string
    def longestCommonSubSequence2(self, S, D):

        D = sorted(D, key=len, reverse=True)
        for word in D:

            current = 0
            for s in S:
                if s == word[current]:
                    current += 1
                    if current > len(word) - 1:
                        return word

    @staticmethod
    def findNextIndex(lst, idx):

        if idx > lst[len(lst)-1]:
            return None

        left = 0
        right = len(lst)
        mid = None
        while left != right:
            mid = (right - left)//2
            if lst[mid] <= idx:
                left = mid + 1
            else:
                right = mid
            
                
        return lst[left]

    def longestCommonSubSequence3(self, S, D):

        s_map = {}
        for i in range(len(S)):
            ch = S[i]
            if not ch in s_map:
                s_map[ch] = []

            s_map[ch].append(i)
        # O(n) at this point

        D = sorted(D, key=len, reverse=True)  # O(m log m)

        # print(s_map)
        for word in D:
            current = -1
            for i in range(len(word)):
                ch = word[i]
                if ch not in s_map:
                    break
                lst = s_map[ch]
                current = Solution.findNextIndex(lst, current) # O(log(m))
                if current == -1:
                    break
            if current != -1:
                return word


S = "abppplee"
D = ["able", "ale", "apple", "bale", "kangaroo", "zulu"]
print(Solution().longestCommonSubSequence3(S, D))
