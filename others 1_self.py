class Trie():
    
    def __init__(self):
        self.root = {}
        self.count = 0
        
    def add(self, string):
        node = self.root
        for char in string:
            if char not in node:
                node[char] = {}
                self.count += 1
            node = node[char]

telephone = Trie()

n = int(input())
for i in range(n):
    telephone.add(input())

print(telephone.count)
