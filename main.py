# This is a sample Python script.
import sys
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def TrieConstruction(Patterns):
    count = 0
    root = TrieNode("", count)
    count += 1
    for pattern in Patterns:
        currentNode = root
        for c in pattern:
            if c not in currentNode.children.keys():
                currentNode.children[c] = TrieNode(c,count)
                count += 1
            currentNode = currentNode.children.get(c)
        currentNode.is_end = True
    return root


#class from github
class TrieNode:
    """A node in the trie structure"""

    def __init__(self, char, count):
        # the character stored in this node
        self.char = char

        # whether this can be the end of a word
        self.is_end = False

        # a counter indicating how many nodes have been inserted
        self.counter = count

        # a dictionary of child nodes
        # keys are characters, values are nodes
        self.children = {}

    def print(self, prev):

        print(str(prev) + " " + str(self.counter) + " " + self.char)
        for n in self.children.values():
            n.print(self.counter)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filePath = input()
    inFile = open(filePath)
    patterns = []
    for line in inFile:
        patterns.extend(line.split())
    inFile.close()
    trie = TrieConstruction(patterns)
    f = open("output.txt", 'w')
    sys.stdout = f
    for node in trie.children.values():
        node.print(0)
    f.close()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
