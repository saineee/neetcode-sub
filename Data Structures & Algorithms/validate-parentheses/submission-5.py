class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {"{": "}", "[": "]", "(": ")"}
        stack = []
        
        for curr in s:
            if curr in lookup:
                stack.append(curr)
            elif curr in lookup.values():
                if not stack or lookup[stack.pop()] != curr:
                    return False
        return len(stack) == 0