# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        # keep a hashmap to store the reverse of each closing bracket
        hashmap = { '}':'{', ']':'[', ')':'(' }

        stack = []

        for ch in s:
            # the below condition is valid if we have already encountered an opening paren
            if ch in hashmap:
                # make sure the stack is non-empty and peek the last element - pop if equal, if non-equal - return False
                if stack and stack[-1] == hashmap[ch]:
                    stack.pop()
                else:
                    return False
            else:
                # push the char to the stack
                stack.append(ch)

        return len(stack) == 0
