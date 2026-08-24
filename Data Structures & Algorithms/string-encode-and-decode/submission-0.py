class Solution:

    def encode(self, strs: List[str]) -> str:
        res = str()

        # basically add a number and pound key before the word
        for word in strs:
            res += str(len(word)) + "#" + word

        return res

    def decode(self, s: str) -> List[str]:
        res_list = list()

        i = 0

        while i < len(s):
            j = i

            while j < len(s) and s[j] != "#":
                j += 1
            # once we break out of loop, we have collected the number
            num = s[i : j]
            str_len = int(num)

            res_list.append(s[j+1 : j + str_len + 1])

            i = j + str_len + 1

        return res_list