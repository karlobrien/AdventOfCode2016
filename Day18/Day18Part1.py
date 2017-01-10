input = '.^^^.^.^^^^^..^^^..^..^..^^..^.^.^.^^.^^....^.^...^.^^.^^.^^..^^..^.^..^^^.^^...^...^^....^^.^^^^^^^'
#input = '.^^.^.^^^^'

def generate_row(prev_row):
    line = ''
    for pos in range(len(prev_row)):
        if pos == 0: #makes sense as left is safe, so take the value of the right tile
            line = line + prev_row[1]
        elif pos == len(prev_row) - 1: #same as the first except at the other end
            line = line + prev_row[len(prev_row) - 2]
        elif prev_row[pos - 1] != prev_row[pos + 1]:
            line = line + '^'
        else:
            line = line + '.'

    return line

def solve(num_rows, row):
    safe_tiles = 0

    for item in range(num_rows):
        for c in row:
            if c == '.':
                safe_tiles += 1
        row = generate_row(row)

    print safe_tiles

total_rows = 40
total_rows = 400000

solve(total_rows, input)