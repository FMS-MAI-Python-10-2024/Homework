def solve():
    grid = [[int(x) for x in input().split()]]
    for _ in range(len(grid[0]) - 1):
        grid.append([int(x) for x in input().split()])

    ans = [[0] * (len(grid[0]) - 2) for _ in range(len(grid) - 2)]

    for i in range(len(ans)):
        for j in range(len(ans[i])):
            ans[i][j] = max(grid[i][j], grid[i][j + 1], grid[i][j + 2], grid[i + 1][j], grid[i + 1][j + 1],
                            grid[i + 1][j + 2], grid[i + 2][j], grid[i + 2][j + 1], grid[i + 2][j + 2])

    return ans