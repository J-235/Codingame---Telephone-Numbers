class Trie():
    def __init__ (self):
        self.children = {None:None} # dictionary with key = character and value = Node object of next node
									# root 	>> self.children = {0: Node object at 0x7fd672cb02b0}
                                    # 0 	>> self.children = {1: Node object at 0x7fd672cb0588}
                                    # 1 	>> self.children = {2: Node object at 0x7fd672cb05c0}
                                    # 2 	>> self.children = {3: Node object at 0x7fd672cb0630}
    
    # check if the character already exists in Trie. 
    # If not, the character will be added to the Trie as child of root or child of a character which already is in Trie
    def insert(node, string, count):
        index_last_c = None
        for index_c, c in enumerate(string):
            if c in node.children:
                node = node.children[c]
            else:
                index_last_c = index_c
                break
        
        if index_last_c is not None:
            for c in string[index_last_c:]:
                node.children[c] = Trie()
                node = node.children[c]
                count += 1
            return count
        else:
            return count
            
root = Trie()
count = 0

n = int(input())
# number of characters which are not yet in Trie will be returned
for i in range(n):
    count = root.insert(input(), count)

print(count)
