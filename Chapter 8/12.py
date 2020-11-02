def place_queens(n,width):
    row = set()
    col = set()
    diag = set()
    pos_lists = []
    memo = set()
    is_right = True
    rec_place_queens(n, width, row, col, diag, 0, 0, [], pos_lists, memo, is_right)

    return pos_lists


def rec_place_queens(n, width, used_rows, used_cols, used_diag, curr_row, curr_col, curr_pos_list, pos_lists, memo, is_right):
    #TODO: BASE CASE
    if n==0:
        pos_lists.append(curr_pos_list)
        return
    if curr_row >= width or curr_col >= width:
        return


    next_row, next_col, next_right = next_pos(curr_row, curr_col, is_right, width)
    #if placement is valid,
    if curr_row not in used_rows and curr_col not in used_cols and (curr_row-curr_col) not in used_diag:
        new_curr_pos_list = curr_pos_list + [(curr_row, curr_col)]
        #go next
        if (not (next_row, next_col, n-1) in memo or True):
            memo.add((next_row, next_col, n-1))
            rec_place_queens(n-1, width, used_rows|{curr_row}, used_cols|{curr_col},
                         used_diag|{curr_row-curr_col}, next_row, next_col, new_curr_pos_list, pos_lists, memo, next_right)


    #go next without using the placement
    if (not (next_row, next_col, n) in memo or True):
        memo.add((curr_row, curr_col, n))
        rec_place_queens(n, width, used_rows, used_cols,
                     used_diag, next_row, next_col, curr_pos_list, pos_lists, memo, next_right)


def next_pos(curr_row, curr_col, is_right, width):
    next_col = curr_col
    next_row = curr_row
    if is_right and curr_col>= width-1:
        next_col -= 1
        next_row += 1
        is_right = False
    elif not is_right and curr_col<=0:
        next_col += 1
        next_row +=1
        is_right = True
    elif is_right:
        next_col += 1
    else:
        next_col -= 1

    return next_row, next_col, is_right


res = (place_queens(2,3))
for r in res:
    print(r)
