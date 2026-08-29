class Solution(object):
    def uniquePathsIII(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        start_row = 0
        start_col = 0
        empty = 0

        # Find starting position and count walkable cells
        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1:
                    start_row = r
                    start_col = c

                if grid[r][c] == 0:
                    empty += 1

        def backtrack(r, c, remaining):

            # Reached ending square
            if grid[r][c] == 2:
                if remaining == 0:
                    return 1
                return 0

            # Mark current cell as visited
            grid[r][c] = -1

            count = 0

            directions = [
                (1, 0),   # down
                (-1, 0),  # up
                (0, 1),   # right
                (0, -1)   # left
            ]

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if (0 <= nr < rows and
                    0 <= nc < cols and
                    grid[nr][nc] != -1):

                    count += backtrack(nr, nc, remaining - 1)

            # Unmark for backtracking
            grid[r][c] = 0

            return count

        return backtrack(start_row, start_col, empty + 1)
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        