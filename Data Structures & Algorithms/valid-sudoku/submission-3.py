class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        list_count_rows = [[0]*9 for i in range(9)]
        list_count_colomns = [[0]*9 for i in range(9)]
        list_count_squares = [[0]*9 for i in range(9)]

        ind_square = -1

        for ind_row in range(9):

            if ind_row < 3:
                ind_square = -1
            elif ind_row < 6:
                ind_square = 2
            else:
                ind_square = 5

            for ind_colomn in range(9):

                if ind_colomn % 3 == 0:
                    ind_square += 1

                if board[ind_row][ind_colomn] != ".":
                    nb = int(board[ind_row][ind_colomn]) - 1

                    if list_count_rows[ind_row][nb] == 1:
                        return False
                    if list_count_colomns[ind_colomn][nb] == 1:
                        return False
                    if list_count_squares[ind_square][nb] == 1:
                        return False

                    list_count_rows[ind_row][nb] += 1

                    list_count_colomns[ind_colomn][nb] += 1

                    list_count_squares[ind_square][nb] += 1
        return True
                    

