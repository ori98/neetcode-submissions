class Solution:
    def isValid(self, s: str) -> bool:
        # base condition is if the length of string is unevenl, then we just return false
        if len(s) % 2 != 0:
            return False
        # brackets dict
        # key = close bracket; value = open bracket
        bracket_dict = {
            "]": "[",
            ")": "(",
            "}": "{",
        }

        # we want FILO for brackets
        bracket_stack = []

        # go through the brackets
        for curr_bracket in s:
            if curr_bracket not in bracket_dict.keys():
                bracket_stack.append(curr_bracket)
            else:# closing  bracketdetected 
                # condition where there are more closing brackets than opening
                if len(bracket_stack) == 0:
                    return False
                last_bracket = bracket_stack.pop(-1)
                corresponding_open_bracket = bracket_dict.get(curr_bracket) 
                print(f"{last_bracket=}")
                print(f"{corresponding_open_bracket=}")
                if last_bracket != corresponding_open_bracket:
                    return False
                # else we continue
                continue
                
        
        # Passes all tollgates
        return True if len(bracket_stack) == 0 else False