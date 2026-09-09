class Solution(object):
    def floodFill(self, image, sr, sc, color):
        old_color = image[sr][sc]

        # Already the same color
        if old_color == color:
            return image

        def dfs(r, c):
            # Boundary check
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                return

            # Only change the original color
            if image[r][c] != old_color:
                return

            image[r][c] = color

            # Up
            dfs(r - 1, c)

            # Down
            dfs(r + 1, c)

            # Left
            dfs(r, c - 1)

            # Right
            dfs(r, c + 1)

        dfs(sr, sc)

        return image