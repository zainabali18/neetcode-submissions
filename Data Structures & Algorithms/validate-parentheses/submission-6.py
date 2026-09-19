class Solution:
    def isValid(self, s: str) -> bool:
        braces = {"(": ")", "{": "}", "[":"]"}
        stack = []
        for brace in s:
            if brace in braces: # open brace
                stack.append(brace)
            else: # closing brace
                if not stack or braces[stack.pop()] != brace:
                    return False
        return not stack
