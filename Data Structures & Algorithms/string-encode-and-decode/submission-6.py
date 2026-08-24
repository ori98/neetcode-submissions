class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            encoded += str(len(word)) + "#" + word
        
        return encoded

    def decode(self, s: str) -> List[str]:
        # base case
        if len(s) == 0:
            return []

        # word format : len + # + word
        ptr = 0
        word_len_str = ""
        decoded_word_list = []

        while (ptr < len(s)):
            # if we get a number
            if s[ptr] >= "0" and s[ptr] <= "9":
                # read until '#'
                while s[ptr] != "#":
                    word_len_str += s[ptr]
                    ptr += 1
                
                # once it is not a number anymore, we read the word
                word_len = int(word_len_str)

                # 2#ab
                # skip the #
                ptr += 1

                start = ptr
                end = ptr + word_len
                word = s[start:end]

                decoded_word_list.append(word)

                ptr = end
                # resets
                word_len_str = ""
            else:
                ptr += 1


        return decoded_word_list