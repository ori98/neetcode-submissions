class Solution:
    def helper(self, word: str) -> dict[str, int]:
        res_dict: dict[str, int] = dict()

        res_freq: dict[str, int] = dict()

        for i in range(0, len(word)):
            # New char
            if word[i] not in res_freq:
                # Store the character : freq = 1
                res_freq[word[i]] = 1
            # old char
            else:
                res_freq[word[i]] += 1
        
        return res_freq

    def isAnagram(self, s: str, t: str) -> bool:
        # if the num of chars are not same
        if len(s) != len(t):
            return False
        
        s_dict = self.helper(s)
        t_dict = self.helper(t)

        return s_dict == t_dict

