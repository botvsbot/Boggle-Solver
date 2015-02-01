class Trie(object):
    def __init__(self):
        self.word = None
        self.children = {}
    def insert(self, word):
        for letter in word:
            if letter not in self.children:
                self.children[letter] = Trie()
            self = self.children[letter]
        self.word = word.lower()
    def prefix_exists(self,word):
        for letter in word.lower():
            if letter not in self.children:
                return False
            self = self.children[letter]
        return True



def dfs(matrix, row, col, visited, current_word):
    visited[row][col] = True
    for k in xrange(row-1,row+2):
        for l in xrange(col-1, col+2):
            if (k >=0 and k < len(matrix)) and (l >= 0 and l < len(matrix)):
                if (not visited[k][l]):
                    current_word.append(matrix[k][l])
                    if "".join(current_word) in words and len(current_word) >= 5:
                        print "".join(current_word)
                    if trie.prefix_exists("".join(current_word)):
                        visited[k][l] = True
                        dfs(matrix, k, l, visited, current_word)
                    else:
                        del(current_word[-1])
                        continue
            else:
                continue
    # Backtracking
    del(current_word[-1])
    visited[row][col] = False


def boggle_dfs(matrix, visited):
    i = 0
    for word in matrix:
        j = 0
        for letter in word:
            current_word = [letter]
            dfs(matrix, i, j, visited, current_word)
            j += 1
            visited = [False for i in xrange(len(matrix))]
            visited = [visited for i in xrange(len(matrix))]
        i += 1

words = open("/usr/share/dict/words").read().split()
matrix = "lkcg eaow mthr ales".split(" ")

trie = Trie()
for word in words:
    trie.insert(word)
print "Trie insertion done"
visited = [False for i in xrange(len(matrix))]
visited = [visited for i in xrange(len(matrix))]
for m in matrix:
    print m
boggle_dfs(matrix, visited)
