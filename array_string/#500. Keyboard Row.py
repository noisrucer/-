class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        hash_table = {
            'q': 0, 'w': 0, 'e': 0, 'r': 0, 't': 0, 'y': 0, 'u': 0, 'i': 0, 'o': 0, 'p': 0,
            'a': 1, 's': 1, 'd': 1, 'f': 1, 'g': 1, 'h': 1, 'j': 1, 'k': 1, 'l':1,
            'z': 2, 'x': 2, 'c': 2, 'v': 2, 'b': 2, 'n': 2, 'm': 2
        }

        res = []

        for word in words:

            same = True
            lower = word.lower()
            for i in range(len(word) - 1):
                if hash_table[lower[i]] != hash_table[lower[i + 1]]:
                    same = False
                    break
            if same == True:
                res.append(word)
        
        return res