class Solution:
    def isValid(self, s: str) -> bool:
       dict_lookup = {"{": "}", "[": "]", "(": ")"}
       stack = []

       for current in s:
        if current in dict_lookup:
            stack.append(current)
        elif current in dict_lookup.values():
            if not stack or dict_lookup[stack.pop()] != current:
                return False
       return len(stack) == 0