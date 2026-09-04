class Solution:
    def numDecodings(self, s: str) -> int:
        index_to_num_decoding_ways = {}
        index_to_num_decoding_ways[len(s)] = 1

        def rec(i):
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0
            if i in index_to_num_decoding_ways:
                return index_to_num_decoding_ways[i]

            res = rec(i+1)
            if i < len(s) - 1 and 10 <= int(s[i:i+2]) <= 26:
                res += rec(i+2)

            index_to_num_decoding_ways[i] = res
            return res

        return rec(0)
