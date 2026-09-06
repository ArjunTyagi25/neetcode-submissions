class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        j = 0

        while True:
            for i in range(len(strs)):
                if i == 0:
                    if j == len(strs[i]):
                        return common_prefix
                    else:
                        curr_char = strs[i][j]
                else:
                    if j == len(strs[i]) or curr_char != strs[i][j]:
                        return common_prefix

            common_prefix += curr_char
            j += 1
            
            

                
            

        