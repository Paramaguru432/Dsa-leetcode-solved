class Solution(object):
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])

        def backtrack(r, c, index):

            # Entire word is found
            if index == len(word):
                return True

            # Outside the board
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            # Wrong character
            if board[r][c] != word[index]:
                return False

            # Mark as visited
            temp = board[r][c]
            board[r][c] = "#"

            # Try 4 directions
            found = (
                backtrack(r + 1, c, index + 1) or
                backtrack(r - 1, c, index + 1) or
                backtrack(r, c + 1, index + 1) or
                backtrack(r, c - 1, index + 1)
            )

            # Undo the change
            board[r][c] = temp

            return found

        for r in range(rows):
            for c in range(cols):

                if board[r][c] == word[0]:

                    if backtrack(r, c, 0):
                        return True

        return False
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        