class Solution:
    _key = 129                      # Fixed XOR key used for encoding/decoding
    _sep = "//"                     # Separator between encoded words
    _empty_list_sentinel = "<EMPTY_LIST>"  # Sentinel string to represent an empty list

    def encode(self, strs: list[str]) -> str:
        # If the input list is None or empty, return the sentinel for empty list
        if strs is None or len(strs) == 0:
            return self._empty_list_sentinel

        encoded_words = []          # List to hold encoded words
        for word in strs:           # Iterate over each string in the list
            encoded_word = []       # List to hold encoded characters of the current word
            for c in word:          # Iterate over each character in the word
                # XOR character ordinal with key and convert back to character
                encoded_word.append(chr(ord(c) ^ self._key))
            # Join the encoded characters of the word into a string
            encoded_words.append("".join(encoded_word))

        # Join all encoded words using the separator and return as single string
        return self._sep.join(encoded_words)

    def decode(self, s: str) -> list[str]:
        # If input string is the empty list sentinel, return an empty list
        if s == self._empty_list_sentinel:
            return []

        decoded_words = []          # List to hold decoded words
        # Split the encoded string by the separator to get individual encoded words
        for word in s.split(self._sep):
            decoded_word = []       # List to hold decoded characters of the current word
            for c in word:          # Iterate over each encoded character
                # XOR again with the key to get original character
                decoded_word.append(chr(ord(c) ^ self._key))
            # Join the decoded characters of the word into a string
            decoded_words.append("".join(decoded_word))

        # Return the full list of decoded strings
        return decoded_words