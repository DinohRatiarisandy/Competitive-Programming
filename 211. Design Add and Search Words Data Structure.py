from collections import defaultdict as dd

class WordDictionary:

    def __init__(self):
        self.dict = dd(list)

    def addWord(self, word: str) -> None:
        self.dict[len(word)].append(word)

    def search(self, word: str) -> bool:
        n = len(word)
        
        if '.' in word:
            for w in self.dict[n]:
                if all(word[i] in (w[i], '.') for i in range(n)):
                    return True
            else:
                return False
            
        return word in self.dict[n]


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)