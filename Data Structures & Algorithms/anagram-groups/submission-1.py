class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        grouped_anagrams = []

        for s in strs:
            key = [0] * 26
            for char in s:
                key[ord(char)-ord('a')] += 1

            if tuple(key) in hash_map:
                hash_map[tuple(key)].append(s)
            else:
                hash_map[tuple(key)] = [s]

        for anagrams in hash_map:
            grouped_anagrams.append(hash_map[anagrams])

        return grouped_anagrams
                    