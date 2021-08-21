# COSC550 Programming Assignment - Sudoku Solver Program

# 2D array representing the sudoku puzzle, with 0 representing cells with no pre-assigned digit.
sudoku = [  [9, 0, 0, 1, 7, 0, 4, 0, 2], 
            [1, 6, 0, 0, 4, 0, 0, 9, 5],
            [0, 0, 8, 0, 0, 3, 0, 0, 0],
            [0, 1, 0, 9, 0, 0, 5, 7, 3],
            [0, 4, 0, 0, 0, 0, 0, 2, 0],
            [5, 8, 9, 0, 0, 7, 0, 1, 0],
            [0, 0, 0, 4, 0, 0, 7, 0, 0],
            [6, 7, 0, 0, 2, 0, 0, 5, 8],
            [3, 0, 1, 0, 5, 8, 0, 0, 6] ]

"""
    The solve_sudoku_puzzle function solves the sudoku puzzle by implementing a Depth First Search.
    The function searches for unassigned cells by calling the search_sudoku function.
    Ints 1-9 are iterated for row and col index of unassigned cell found.
    The row_match, col_match and box_match functions are called to search for matches for the int range.
    If no match is found, the int is assigned to the cell.
    The function is called recursively, and if matches are found for all digits, the next cell is reassigned to 0.
    Function returns true if no more unassigned cells are found.
    @param sudoku a 2D array representing the sudoku puzzle.
"""
def solve_sudoku_puzzle(sudoku):
    print("\n________________________________________")
    print("\nSearching for unassigned cell:\n")
    # Calls search_empty function to search sudoku puzzle for unassigned cells.
    if not search_empty(sudoku):
        # Returns true if no unassigned cells in sudoku puzzle.
        print("Sudoku puzzle is solved: \n")
        print_sudoku(sudoku)
        return True
    else:
        """
            If unassigned cell found, assigns index returned by search function to variables:
            empty_row_index int representing row index of unassigned cell returned by search function.
            empty_col_index int representing col index of unassigned cell returned by search function.
        """
        empty_row_index, empty_col_index = search_empty(sudoku)
        print("Found unassigned cell at row:", empty_row_index, "col:", empty_col_index, "\n")
        print("Checking for matches in row, col and 3x3 range box:\n")
    # Iterates ints between 1-9 to check for matches in sudoku row, col, and 3x3 box.
    #print("Iterating digits 1-9 for placement in empty cell.\n")
    for digit in range(1, 10):
        # Calls row_match, col_match and box_match functions to check for matches with digits 1-9._________
        if not row_match(sudoku, empty_row_index, empty_col_index, digit) and not col_match(sudoku, empty_row_index, empty_col_index, digit) and not box_match(sudoku, (empty_row_index-empty_row_index%3), (empty_col_index-empty_col_index%3), digit):
            print("\nNo match for digit", digit, ". Assigning", digit, "to row:", empty_row_index, "col:", empty_col_index, "\n")
            # Assigns digit to unassigned cell index if no matches found.
            sudoku[empty_row_index][empty_col_index] = digit
            print("Updated state of sudoku puzzle:\n")
            print_sudoku(sudoku)
            # Recursive call to solve_sudoku_puzzle function with updated sudoku puzzle, returns true if all cells assigned.
            if solve_sudoku_puzzle(sudoku):
                return True
            # If sudoku puzzle not solved, re-assigns 0 to indexed cell.
            print("\nDigits 1-9 all found match, re-assigning row", empty_row_index, "col", empty_col_index, "to 0.\n")
            sudoku[empty_row_index][empty_col_index] = 0
    return False

"""
    The print_sudoku function displays the current state of the sudoku puzzle.
    @param sudoku a 2D array representing the sudoku puzzle.
"""
def print_sudoku(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            print(sudoku[i][j], " ", end='')
        print()

"""
    The search_empty function searches a 2D array for unassigned cells represented by 0.
    Returns false if no unassigned cells, else returns the row and col index of next unassigned cell.
    @param sudoku a 2D array representing the sudoku puzzle.
"""
def search_empty(sudoku):
    # Nested for loop iterates rows and columns of 2D array.
    for row in range(9):
        for col in range(9):
            # Returns row and col index of unassigned cell if finds value of 0.
            if sudoku[row][col] == 0:
                #print("Found unassigned cell at row:", row, "column:", col, "\n")
                return (row, col)     
    print("There are no unassigned cells left.\n")
    return False

"""
    The row_match function iterates a 2D array to check for match of an int in a row.
    Returns true if match found for int in given row index.
    @param sudoku a 2D array represnting the sudoku puzzle.
    @param empty_row_index int representing row index of an unassigned cell in 2D array.
    @param empty_col_index int representing col index of an unassigned cell in 2D array.
    @param digit int being checked for matches.
"""
def row_match(sudoku, empty_row_index, empty_col_index, digit):
    # Iterating 2D array row by column index.
    for col in range(len(sudoku)):
        # Returns true if value matching digit is found in row.
        if sudoku[empty_row_index][col] == digit:
            print("Row match found for digit", digit)
            return True

"""
    The col_match function iterates a 2D array to check for match of an int in a col.
    Returns true if match found for int in given col index.
    @param sudoku a 2D array represnting the sudoku puzzle.
    @param empty_row_index int representing row index of an unassigned cell in 2D array.
    @param empty_col_index int representing col index of an unassigned cell in 2D array.
    @param digit int being checked for matches.
"""
def col_match(sudoku, empty_row_index, empty_col_index, digit):
    # Iterating 2D array col by row index.
    for row in range(len(sudoku)):
        # Returns true if value matching digit is found in col.
        if sudoku[row][empty_col_index] == digit:
            print("Col match found for digit", digit)
            return True

"""
    The box_match function iterates a 2D array to check for match of an int in cells 3x3 in a range.
    Returns true if match found for int in 3x3 range of given row and col index.
    @param sudoku a 2D array represnting the sudoku puzzle.
    @param empty_row_index int representing row index of an unassigned cell in 2D array.
    @param empty_col_index int representing col index of an unassigned cell in 2D array.
    @param digit int being checked for matches.
"""
def box_match(sudoku, empty_row_index, empty_col_index, digit):
    # box_size int representing range of indexes being checked.
    box_size = 3
    # Nested for loop iterating indexes for size of 3x3 box around given row and col indexes.
    for row in range(box_size):
        for col in range(box_size):
            # Returns true if value matching digit is found in 3x3 range.
            if sudoku[row+empty_row_index][col+empty_col_index] == digit:
                #print("MATCH IN BOX. Digit:", digit, "row 0-2 of box:", row, "col 0-2 of box:", col)
                print("Match found in 3x3 range for digit", digit)
                return True

def main():
    print("\nWelcome to the Sudoku Solver Program \n")
    print("Author: Bianca Davey, bdavey2@myune.edu.au \n")
    print("This program implements a Depth First Search to solve a Sudoku puzzle. \n")
    print("Method to solve problem:\n")
    print("*    The solve_sudoku function is called to solve the sudoku puzzle, taking sudoku as an arg.")
    print("*    The function searches for next unassigned cell by calling the search_empty function.")
    print("*    The search_empty function takes sudoku as an arg and iterates 2D array by row and col to search for an empty cell.")
    print("*    If unassigned cell found, index is returned, else False is returned.")
    print("*    solve_sudoku then iterates ints 1-9, calling row_match, col_match and box_match functions to check for matches with ")
    print("     int in row, col and 3x3 box index range of unassigned cell index.")
    print("*    The row_match, col_match and box_match functions iterate the sudoku puzzle for matches with given int.")
    print("*    If no match is found in row, col or box, int is assigned to the indexed cell.")
    print("*    solve_sudoku function is called recursively, and if matches are found for all int 1-9, cell is reassigned to 0.")
    print("*    Function returns True if no more unassigned cells are found.\n")
    print("List of params:\n")
    print("*    sudoku: a 2D array representing a 9x9 sudoku puzzle, with 0 representing unassigned cells.")
    print("*    empty_row_index: an int representing a row index of an unassigned cell returned by the search_empty function.")
    print("*    empty_col_index: an int representing a col index of an unassigned cell returned by the search_empty function.")
    print("*    box_range: an int representing the range of indexes being searched around a given row and col index.\n")
    print("\n________________________________________\n")
    print("Starting analysis: \n")
    # Displaying initial unsolved state of sudoku puzzle.
    print("Initial state of sudoku puzzle: \n")
    print_sudoku(sudoku)
    print()
    # Implementing the search to solve the sudoku puzzle.
    print("Implementing search to solve sudoku puzzle:") 
    solve_sudoku_puzzle(sudoku)

if __name__ == "__main__":
    main()