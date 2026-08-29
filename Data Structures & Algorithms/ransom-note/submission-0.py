class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_hash_map = {}
        for c in magazine:
            magazine_hash_map[c] = 1 + magazine_hash_map.get(c, 0)

        for c in ransomNote:
            if c not in magazine_hash_map:
                return False
            else:
                magazine_hash_map[c] -= 1
                if magazine_hash_map[c] < 0:
                    return False

        return True
        