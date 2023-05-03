from typing import List


def count_islands(grid: List[List[str]]) -> int:
    """
    Returns the number of islands in a 2D binary grid.

    An island is a group of '1's (land) that are adjacent
    horizontally or vertically and are surrounded by '0's (water).
    The grid is represented as a list of lists, where each inner list
    represents a row and contains '0's or '1's.

    Args:
        grid (List[List[str]]): A 2D binary grid represented as a list
                                of lists of '0's and '1's.

    Returns:
        int: The number of islands in the grid.

    Example:
        >>> grid = [['1', '1', '1', '1', '0'],
                    ['1', '1', '0', '1', '0'],
                    ['1', '1', '0', '0', '0'],
                    ['0', '0', '0', '0', '0']]
        >>> count_islands(grid)
        1
    """

    if not grid:
        return 0

    def dfs(i: int, j: int) -> None:
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) \
                or grid[i][j] != '1':
            return

        grid[i][j] = '#'

        dfs(i - 1, j)  # UP
        dfs(i + 1, j)  # DOWN
        dfs(i, j - 1)  # LEFT
        dfs(i, j + 1)  # RIGHT

    result = 0
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == '1':
                dfs(i, j)
                result += 1

    return result


if __name__ == "__main__":
    assert count_islands(
        [
            ['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0'],
        ]
    ) == 1

    assert count_islands(
        [
            ['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']
        ]
    ) == 3
