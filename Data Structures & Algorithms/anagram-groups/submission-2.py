class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_of_strs = {}
        res = []

        for s in strs:
            freq_of_s = [0]*26

            for c in s:
                freq_of_s[ord(c)-ord('a')] += 1

            key = tuple(freq_of_s)
            if key in freq_of_strs:
                freq_of_strs[key].append(s)
            else:
                freq_of_strs[key] = [s]

        for k, v in freq_of_strs.items():
            res.append(v)

        return res        

        