class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = []
        sorted_str_to_index = {} # sorted str as key, index in grouped_anagram as value
        count = 0

        for i in range(len(strs)):
            sorted_str = ''.join(sorted(strs[i]))

            if sorted_str in sorted_str_to_index:
                grouped_anagrams[sorted_str_to_index[sorted_str]].append(strs[i])
            else:
                grouped_anagrams.append([strs[i]])
                sorted_str_to_index[sorted_str] = count
                count += 1

        return grouped_anagrams
        