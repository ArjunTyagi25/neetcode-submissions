class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) <= len(text2):
            smallerStr, longerStr = text1, text2
        else:
            smallerStr, longerStr = text2, text1

        memo = {}
        def rec(i, j):
            if i == len(smallerStr) or j == len(longerStr):
                return 0

            if (i,j) in memo:
                return memo[(i,j)]

            if smallerStr[i] == longerStr[j]:
                res = 1 + rec(i+1, j+1)
            else:
                # Skip the character in longerStr
                res_1 = rec(i, j+1)

                # Skip the character in smallerStr
                res_2 = rec(i+1, j)

                res = max(res_1, res_2)

            memo[(i,j)] = res
            return res
        return rec(0, 0)

'''
            Find which string is the smaller of the two and let that be smallerStr and the other be longerStr.
            Given two pointers i and j pointing to characters in string smallerStr and longerStr respectively, I have the following choices:
        - If smallerStr[i] == longerStr[j], do 1 + rec(i+1, j+1)
        - If they are not equal, we can either delete a character in longerStr (so rec(i, j+1)) or start a new subsequence
            '''


