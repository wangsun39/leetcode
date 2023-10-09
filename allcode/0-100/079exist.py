from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        line, column = len(board), len(board[0])
        def tryOneNode(i, j, word):
            if board[i][j] == word[0]:
                board[i][j] = 0
                if recurFind(i, j, word[1:]):
                    print(i, j)
                    return True
                else:
                    board[i][j] = word[0]
                    return False
            return False
        def recurFind(i, j, word):
            if word == '':
                return True
            if i > 0:
                if tryOneNode(i-1, j, word):
                    return True
                # if board[i-1][j] == word[0]:
                #     board[i - 1][j] = 0
                #     if recurFind(i-1, j, word[1:]):
                #         return True
                #     else:
                #         board[i - 1][j] = word[0]
            if i < line - 1:
                if tryOneNode(i+1, j, word):
                    return True
            if j > 0:
                if tryOneNode(i, j-1, word):
                    return True
            if j < column - 1:
                if tryOneNode(i, j+1, word):
                    return True
        for i in range(line):
            for j in range(column):
                if board[i][j] == word[0]:
                    board[i][j] = 0
                    if recurFind(i, j, word[1:]):
                        print(i, j)
                        return True
                    else:
                        board[i][j] = word[0]
        return False

so = Solution()
print(so.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], "SEE"))
print(so.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], "ABCCED"))
print(so.exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], "ABCB"))

