class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        dict_fermeture = {"]": "[", "}": "{", ")": "("}

        for el in s:
            if el == "[" or el == "{" or el == "(":
                stack.append(el)
            else:
                if not stack:
                    return False
                elif stack[-1] == dict_fermeture[el]:
                    stack.pop()
                else:
                    return False
                    
        return not stack