from random import choice
from prefixtree import PrefixTree
 
class Boggle(object):
    def __init__(self, board=None):
        self.size = 4
        if board is None:
            self.board = []
            for i in range(0, self.size):
                self.board.append([])
                for j in range(0, self.size):
                    self.board[i].append(Boggle.random_letter())
        else:
            self.board = board
 
    def random_letter():
        return chr(choice(range(65,91)))
 


    def play(self, tree, found):
        for r in range(0, self.size):
            for c in range(0, self.size):
                self.search_r(tree, found, r, c)

                
 
    def search_r(self, tree, found, row, col, path=None, node=None, word=None):
        letter = self.board[row][col]
        if node is None or path is None or word is None:
            node = tree.find_letter(letter)
            path = [(row, col)]
            word = letter
        else:
            node = node.find_letter(letter)
            path.append((row, col))
            word = word + letter
        if node is None:
            return
        elif node.stop:
            found.add(word)
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if (r >= 0 and r < self.size
                        and c >= 0 and c < self.size 
                        and not (r == row and c == col) 
                        and (r, c) not in path):
                    self.search_r(tree, found, r, c, path[:], node, word[:])
 
    def __repr__(self):
        return "Boggle(size={0}, board={1})".format(self.size, self.board)



def load_tree(tree):
    with open('wordlist.txt') as f:
        for line in f:
            word = line.rstrip().upper()
            tree.add(word)
 
def main():
    boggle = Boggle()
    tree = PrefixTree()
    load_tree(tree)
    found = set()
    boggle.play(tree, found)
    for word in sorted(found):
        print(word)
    print(boggle)
 
if __name__ == '__main__':
    main()
