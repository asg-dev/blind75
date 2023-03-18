# Time Complexity: O(n) [ n + n essentially ]
# Space Complexity: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # have a character hashmap to store frequencies
        char_map = {}

        # keep track of frequencies in 's'
        for ch in s:
            char_map[ch] = (char_map[ch] + 1) if ch in char_map else 1

        # for each character in 't'
        for ch in t:
            # decrement if character is in char_map - delete the key if value reaches 0
            if ch in char_map:
                char_map[ch] -= 1
                if char_map[ch] == 0: del char_map[ch]
            else: # early return false as we have encountered a character not already present in 's'
                return False

        # expect length of char_map to be 0
        return len(char_map) == 0
