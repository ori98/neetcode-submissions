class Solution:
    def isValid(self, s: str) -> bool:
        pairs_dict = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        bracket_stack = []

        for bracket in s:
            # a closing bracket
            if bracket in pairs_dict:
                # first we check our stack isn't empty
                if not bracket_stack:
                    return False
                latest_bracket = bracket_stack.pop(-1)
                if latest_bracket != pairs_dict.get(bracket):
                    return False
            else:
                # a opening bracket
                bracket_stack.append(bracket)

        return not bracket_stack