class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0

        for i in range(len(words)):
            first_word = words[i]
            n = len(first_word)

            for j in range(i+1, len(words)):
                second_word = words[j]
                m = len(second_word)

                if n > m:
                    continue

                if first_word == second_word[0:n] and first_word == second_word[m-n:]:
                    res += 1

        return res

                
        