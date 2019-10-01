class Node():
    def __init__(self, val=None):
        self.children = {}
        self.value = val
        self.isWord = False

class Trie():
    def __init__(self):
        self.root = Node()

    def search(self, word):
        '''Return True is word is in Trie, False otherwise'''
        current = self.root
        for i in range(len(word)):
            if word[i] not in current.children:
                return False
            else:
                current = current.children[word[i]] # Traverse the trie
        
        return True if current.isWord else False
        

    def add(self, word):
        current = self.root
        i = 0
        # Traversing through the tree as far as possible, for each of the letters present in trie
        while i < len(word):
            if word[i] in current.children: # Does the node for that letter exist in children?
                current = current.children[word[i]]
                i += 1
            else: # The node for that letter wasn't found - Add node(s)
                break
        # Append new nodes for the remaining characters in the str, if any
        while i < len(word):
            current.children[word[i]] = Node(word[i]) # Create the node
            current = current.children[word[i]] # Traverse to that newly created node
            i += 1
        # Mark the isWord flag to true for the terminal node
        current.isWord = True

    def delete(self, word):
        current = self.root
        i = 0
        # Traversing through the tree as far as possible, for each of the letters present in trie
        while i < len(word):
            if word[i] in current.children: # Does the node for that letter exist in children?
                current = current.children[word[i]]
                i += 1
            else: # The word you're trying to delete isn't present in the Trie!
                return False
        # current at this point should be the word i'm trying to 'delete'
        current.isWord = False
        # Alternative implementations:
        # 1. We delete that current node
        # 2. We traverse up the tree and delete nodes until we find a "word" w/ isWord == true

t = Trie()
t.add('Cow')
print(t.root.children['C'].value)
print(t.root.children['C'].children['o'].value)
print(t.root.children['C'].children['o'].children['w'].value)
# t.add('Cower')
print(t.search("Cow"))
t.delete('Cow')
print(t.search('Cow'))