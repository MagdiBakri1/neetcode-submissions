from typing import List
import string

class Solution:

    def encode(self, strs: List[str]) -> str:
        letters_list = list(string.ascii_lowercase)
        L_S = []

        for i in strs:
            s = ""

            for j in i:
                if j.lower() in letters_list:
                    if j.islower():
                        j = j.lower()
                        s = s + letters_list[
                            (letters_list.index(j) + 3) % 26
                        ]
                    else:
                        j = j.lower()
                        U = letters_list[
                            (letters_list.index(j) + 3) % 26
                        ]
                        s = s + U.upper()
                else:
                    s = s + j

            L_S.append(s)

        result = ""

        for word in L_S:
            result += str(len(word)) + "#" + word

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        letters_list = list(string.ascii_lowercase)

        while i < len(s):

            # نجيب طول الكلمة
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            # بداية الكلمة
            start = j + 1

            # نهاية الكلمة
            end = start + length

            word = s[start:end]

            # Caesar decode
            decoded = ""

            for char in word:
                if char.lower() in letters_list:

                    if char.islower():
                        decoded += letters_list[
                            (letters_list.index(char) - 3) % 26
                        ]

                    else:
                        char = char.lower()

                        U = letters_list[
                            (letters_list.index(char) - 3) % 26
                        ]

                        decoded += U.upper()

                else:
                    decoded += char

            result.append(decoded)

            i = end

        return result