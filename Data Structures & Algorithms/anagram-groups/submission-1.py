class Solution:
    def convert_word_to_tuple(self, word: str) -> tuple:
        # dict(tuple(0,0,1,..,), [])

        # since there are 26 letters in alphabet
        # each index represent a letter with the value as count
        counter = [0] * 26

        # we will convert this later to tuple to make it hashable
        for i in range(0, len(word)):
            word_ptr = ord(word[i]) - ord("a")

            # increment value at the pointer 
            counter[word_ptr] += 1
        
        # converting to hashable tuple
        return tuple(counter)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grouped_dict = dict()

        for word in strs:
            sorted_word_key = self.convert_word_to_tuple(word)

            # create the dict or append to it
            try:
                grouped_dict[sorted_word_key].append(word)
            except KeyError:
                grouped_dict[sorted_word_key] = [word]
        
        grouped_anagram = []
        for key, value in grouped_dict.items():
            grouped_anagram.append(value)
        
        return grouped_anagram