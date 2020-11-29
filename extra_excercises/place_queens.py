rows = [0] * 8
cols = [0] * 8
diag1 = {
    -7: 0,
    -6: 0,
    -5: 0,
    -4: 0,
    -3: 0,
    -2: 0,
    -1: 0,
     0: 0,
     1: 0,
     2: 0,
     3: 0,
     4: 0,
     5: 0,
     6: 0,
     7: 0,
}
diag2 = [0] * 15


def is_valid(row, col):
    if rows[row] == 1 \
        or cols[col] == 1 \
        or diag1[row - col] == 1 \
        or diag2[row + col] == 1:
        return False
    return True


def place_queen(row, col):
    # Invalidate all squares on the same row
    rows[row] = 1
    # Invalidate all squares on the same column
    cols[col] = 1
    # Invalidate all squares on the same diagonal 1 (NW - SE)
    diag1[row - col] = 1
    # Invalidate all squares on the same diagonal 2 (NE - SW)
    diag2[row + col] = 1


def displace_queen(row, col):
    # Validate all squares on the same row
    rows[row] = 0
    # Validate all squares on the same column
    cols[col] = 0
    # Validate all squares on the same diagonal 1 (NW - SE)
    diag1[row - col] = 0
    # Validate all squares on the same diagonal 2 (NE - SW)
    diag2[row + col] = 0


def print_board(*cols):
    for i in range(0, 8):
        for j in range(0, 8):
            if j == cols[i]:
                print('X', end='')
            else:
                print('-', end='')
            if j != 7:
                print('|', end='')
        print('\n')
    print('\n')


def place_queens():
    for col_r0 in range(0, 8):
        if is_valid(0, col_r0):
            place_queen(0, col_r0)
            for col_r1 in range(0, 8):
                if is_valid(1, col_r1):
                    place_queen(1, col_r1)
                    for col_r2 in range(0, 8):
                        if is_valid(2, col_r2):
                            place_queen(2, col_r2)
                            for col_r3 in range(0, 8):
                                if is_valid(3, col_r3):
                                    place_queen(3, col_r3)
                                    for col_r4 in range(0, 8):
                                        if is_valid(4, col_r4):
                                            place_queen(4, col_r4)
                                            for col_r5 in range(0, 8):
                                                if is_valid(5, col_r5):
                                                    place_queen(5, col_r5)
                                                    for col_r6 in range(0, 8):
                                                        if is_valid(6, col_r6):
                                                            place_queen(6, col_r6)
                                                            for col_r7 in range(0, 8):
                                                                if is_valid(7, col_r7):
                                                                    place_queen(7, col_r7)
                                                                    print_board(col_r0, col_r1, col_r2, col_r3, col_r4, col_r5, col_r6, col_r7)
                                                                    displace_queen(7, col_r7)
                                                            displace_queen(6, col_r6)
                                                    displace_queen(5, col_r5)
                                            displace_queen(4, col_r4)
                                    displace_queen(3, col_r3)
                            displace_queen(2, col_r2)
                    displace_queen(1, col_r1)
            displace_queen(0, col_r0)

if __name__ == "__main__":
    place_queens()
