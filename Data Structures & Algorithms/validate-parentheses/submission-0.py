class Solution:
    def isValid(self, t: str) -> bool:
        
        stack = []
        paired_brackets = {"(":")", "[":"]", "{":"}"}
        for bracket in t:
            if bracket in paired_brackets:
                stack.append(bracket)
            else:
                if len(stack) == 0 or paired_brackets[stack.pop()] != bracket:
                    return False
        return len(stack) == 0
