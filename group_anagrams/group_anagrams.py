from typing import List


# Time Complexity: O(n) (excluding sort time complexity)
# Space Complexity: O(1)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for s in strs:
            # sort the current string to set as key in the hashmap
            sortedStr = "".join(sorted(s))
            # if already present, store the original string
            if sortedStr in hashmap:
                hashmap[sortedStr].append(s)
            else:
                # else create a new array with the current element
                hashmap[sortedStr] = [s]
        result = hashmap.values()

        return result
