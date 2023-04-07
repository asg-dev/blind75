from typing import List

# Intuition: Essentially a graph problem. Find indegree and outdegree for each person in the town
# and check the conditions -> find index of indegree for n - 1 i.e. everyone except the town judge
# and check respective outdegree of that node. The outdegree must be 0 for that person to be the
# town judge.

# This can also be solved without the outdegree array - decrement the indegree array by doing another
# pass over the input and check if the town judge identified by the indegree array is still the same.

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n == 1:
            return 1

        # build indegree and outdegree
        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)

        for i, j in trust:
            indegree[j] += 1
            outdegree[i] += 1

        indegree_at = indegree.index(n - 1) if n - 1 in indegree else -1
        if indegree_at > 0 and outdegree[indegree_at] == 0: return indegree_at
        else: return -1

    def findJudge(self, n: int, trust: List[List[int]], without_second_array = True) -> int:
        if not trust and n == 1:
            return 1

        # build indegree
        indegree = [0] * (n + 1)

        for i, j in trust:
            indegree[j] += 1

        indegree_at = indegree.index(n - 1) if n - 1 in indegree else -1

        if indegree_at <= 0:
            return -1

        for i, j in trust:
            indegree[i] -= 1

        if indegree[indegree_at] == n - 1: return indegree_at
        else: return -1
