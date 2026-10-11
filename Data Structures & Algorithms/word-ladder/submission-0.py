class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordsSet = set(wordList)

        q = deque([beginWord])
        visited = set()
        visited.add(beginWord)
        res = 1

        while q:
            for _ in range(len(q)):
                currWord = q.popleft()

                if currWord == endWord:
                    return res

                for i in range(len(beginWord)):
                    for j in range(97, 97+26):
                        nextWord = currWord[:i] + chr(j) + currWord[i+1:]

                        if (nextWord in wordsSet) and nextWord not in visited:
                            q.append(nextWord)
                            visited.add(nextWord)

            res += 1

        return 0