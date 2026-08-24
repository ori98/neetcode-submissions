class Solution:
    def get_sorted_word(self, word: str) -> str:
        sorted_word = ""
        # first we convert the word to char array
        word_char_array = list(word)

        # sort it
        sorted_word_char_array = sorted(word_char_array)

        # then we recreate the word
        sorted_word = ''.join(sorted_word_char_array)

        return sorted_word

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we will have a dict where key is sorted word
        # value is a list of the actual word
        grouped_anagram_dict = dict()
        for word in strs:
            sorted_word = self.get_sorted_word(word)

            # can be used as key for a dict with the actual value in a list
            # as the value
            if sorted_word not in grouped_anagram_dict:
                grouped_anagram_dict[sorted_word] = [word]
            else:
                grouped_anagram_dict[sorted_word].append(word)
            
        # iterate through the values and return it
        grouped_anagram_list = []

        for key, value in grouped_anagram_dict.items():
            grouped_anagram_list.append(value)
        
        return grouped_anagram_list


            
        