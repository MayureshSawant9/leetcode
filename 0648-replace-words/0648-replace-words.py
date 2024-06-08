class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

            
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]

        current.is_end = True

    def search(self, word):
        current = self.root
        prefix = ''
        for letter in word:
            if letter not in current.children:
                return word
            prefix += letter
            if current.children[letter].is_end:
                return prefix
            current = current.children[letter]
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        result = []
        for word in sentence.split(' '):
            result.append(trie.search(word))
        
        return ' '.join(result)

        