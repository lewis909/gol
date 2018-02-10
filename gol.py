def check_neighbour(result):
    if result == 2:
        return 1
    if result > 2:
        return 0
    else:
        return 0


def check_top_left_cell(row, matrix, rn):
    result = 0

    if matrix[0][1] == 1:
        result += 1
    if matrix[rn + 1][1] == 1:
        result += 1
    if matrix[rn + 1][0] == 1:
        result += 1

    row[0] = check_neighbour(result)


def check_top_right_cell(row, matrix, rn):
    x = len(row) - 1
    if row[x] == 0:
        result = 0

        if matrix[0][x - 1] == 1:
            result += 1
        if matrix[rn + 1][x - 1] == 1:
            result += 1
        if matrix[rn + 1][x] == 1:
            result += 1

        row[x] = check_neighbour(result)


def check_bottom_left_cell(row, matrix):
    x = len(row) - 1
    result = 0

    if matrix[x][1] == 1:
        result += 1
    if matrix[x - 1][1] == 1:
        result += 1
    if matrix[x - 1][0] == 1:
        result += 1

    row[0] = check_neighbour(result)


def check_bottom_right_cell(row, matrix, rn):
    x = len(row) - 1
    y = len(matrix) - 1
    if row[x] == 0:
        result = 0
        if matrix[y][x - 1] == 1:
            result += 1
        if matrix[y - 1][x - 1] == 1:
            result += 1
        if matrix[y - 1][x - 1] == 1:
            result += 1

        row[y] = check_neighbour(result)


def check_top_middle_cells(matrix, rn):
    row = matrix[rn][1:-1]
    for cn, cell in enumerate(row):
        result = 0
        if matrix[rn][cn] == 1:
            result += 1
        if matrix[rn][cn + 2] == 1:
            result += 1
        if matrix[rn + 1][cn] == 1:
            result += 1
        if matrix[rn + 1][cn + 1] == 1:
            result += 1
        if matrix[rn + 1][cn + 2] == 1:
            result += 1
        row[cn] = check_neighbour(result)


def check_middle_cells(matrix, rn):
    row = matrix[rn][1:-1]
    for cn, cell in enumerate(row):
        result = 0
        if matrix[rn][cn] == 1:
            result += 1
        if matrix[rn][cn + 2] == 1:
            result += 1
        if matrix[rn + 1][cn] == 1:
            result += 1
        if matrix[rn + 1][cn + 1] == 1:
            result += 1
        if matrix[rn + 1][cn + 2] == 1:
            result += 1

        if matrix[rn - 1][cn] == 1:
            result += 1
        if matrix[rn - 1][cn + 1] == 1:
            result += 1
        if matrix[rn - 1][cn + 2] == 1:
            result += 1
        #print('row:{}, cell:{}, n:{}, res:{}'.format(rn, cn, result, check_neighbour(result)))
        '''if rn == 5 and cell == 1:
            import pdb;pdb.set_trace()'''
        matrix[rn][cn] = check_neighbour(result)


def check_bottom_middle_cells(row, matrix, rn):
    for c, cell in enumerate(row[1:-1]):
        if cell == 1:
            row[c + 1] = 1


def check_right_cell(row, matrix, rn):
    if row[0] == 1:
        row[0] = 1


def check_left_cell(row, matrix, rn):
    x = len(row) - 1
    if row[x] == 1:
        row[x] = 1


def testing(n):

    matrix = [[0 for cell in range(n)] for row in range(n)]
    # top left
    matrix[0][0] = 0
    matrix[0][1] = 0
    matrix[1][1] = 1
    matrix[1][0] = 1
    # top right
    matrix[0][9] = 0
    matrix[1][8] = 1
    matrix[1][9] = 1
    matrix[0][8] = 1
    # bottom left
    matrix[9][0] = 0
    matrix[8][1] = 0
    matrix[8][0] = 1
    matrix[9][1] = 1
    # bottom right
    matrix[9][9] = 0
    matrix[9][8] = 1
    matrix[8][9] = 1
    matrix[8][8] = 1
    # top middle
    matrix[0][5] = 1
    matrix[1][5] = 1
    matrix[1][4] = 1
    matrix[1][6] = 1
    # top middle
    matrix[5][5] = 0
    matrix[5][0] = 0
    matrix[5][6] = 1
    matrix[6][6] = 1

    t = range(n)
    turn = 0
    while turn < 10000:
        print(turn)
        for r, row in enumerate(matrix):

            if r == t[0]:
                # Check top row minus the corners.

                check_top_left_cell(row, matrix, r)
                check_top_middle_cells(matrix, r)
                check_top_right_cell(row, matrix, r)

            if t[0] < r < t[-1]:
                # Check rows in the center of the matrix
                check_left_cell(row, matrix, r)
                check_middle_cells(matrix, r)
                check_right_cell(row, matrix, r)

            if r == t[-1]:

                # Check bottom row minus the corners.

                check_bottom_left_cell(row, matrix)
                check_bottom_middle_cells(row, matrix, r)
                check_bottom_right_cell(row, matrix, r)
        turn += 1
    return matrix

print()
print()
for i in testing(10):
    print(i)