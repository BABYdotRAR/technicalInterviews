# given an int N as input, determine if an spiral can be printed as shown
# N=9    1 2 3
#        8 9 4
#        7 6 5    if it can be printed, print it
import math
import sys


def validate_and_print(n):
    if not has_exact_sqrt(n):
        print("the spiral cannot be printed with the input provided")
        return
    
    _n = int(math.sqrt(n))
    output_matrix = [[None for _i in range(_n)] for _j in range(_n)]
    total_iterations = 2 * _n - 1
    row_flag = True
    available_row_dict = [True for i in range(_n)]
    available_col_dict = [True for i in range(_n)]
    row_pick_asc_order = True
    col_pick_asc_order = False
    row_asc_order = True
    col_asc_order = True
    current_count = 0

    for i in range(total_iterations):
        if row_flag:
            row_flag = False
            order = 'asc' if row_pick_asc_order else 'desc'
            row = get_first_available_index(available_row_dict, order)
            current_count  = fill_row(output_matrix, row, row_asc_order, current_count)
            row_pick_asc_order = not row_pick_asc_order
            row_asc_order = not row_asc_order
        else:
            row_flag = True
            order = 'asc' if col_pick_asc_order else 'desc'
            col = get_first_available_index(available_col_dict, order)
            current_count = fill_col(output_matrix, col, col_asc_order, current_count)
            col_pick_asc_order = not col_pick_asc_order
            col_asc_order = not col_asc_order
    
    for i in range(_n):
        [print(str(j) + "\t", end="") for j in output_matrix[i]]
        print("")


def fill_row(matrix, row, asc_order, current_count):
    start = 0 if asc_order else len(matrix[0]) - 1
    end = len(matrix[0]) if asc_order else -1
    step = 1 if asc_order else -1   
    for i in range(start, end, step):
        current_count = current_count + 1 if matrix[row][i] is None else current_count
        matrix[row][i] = current_count if matrix[row][i] is None else matrix[row][i]
    return current_count


def fill_col(matrix, col, asc_order, current_count):
    start = 0 if asc_order else len(matrix[0]) - 1
    end = len(matrix[0]) if asc_order else -1
    step = 1 if asc_order else -1    
    for i in range(start, end, step):
        current_count = current_count + 1 if matrix[i][col] is None else current_count
        matrix[i][col] = current_count if matrix[i][col] is None else matrix[i][col]
    return current_count


def get_first_available_index(dict:list, order='asc'):
    if order == 'asc':
        for i in range(len(dict)):
            if dict[i]:
                dict[i] = False
                return i
    elif order == 'desc':
        for i in range(len(dict) - 1, -1, -1):
            if dict[i]:
                dict[i] = False
                return i
    return -1


def has_exact_sqrt(n):
    sqrt = math.sqrt(n)
    return sqrt.is_integer()


if __name__ == "__main__":
    n = int(sys.argv[1])
    validate_and_print(n)
