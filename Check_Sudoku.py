'''
   Iterate through the list and count the appearance of a number. If it occurs more than once or the number in at the index is out of range show an error.
   The Sudoku datastructure is defined through a list, which contains lists as elements.
   These elements represent an field, in which there mustn't appear one number twice or more.
   These fields are represented by lists, which contain the numbers from the left to the right.
'''
def check_sudo(sudo):

    """
    Local variables
    """
    length_of_one_field = len(sudo[0])  # Get the length of the sudoku list for the number of checking iterations
    length_whole_sudoku = len(sudo)     # Get the count of all smallest sudoku entities
    field = 0                           # Current watched field
    index = 0                           # Current index of the list
    number = 1                          # Current searched number
    counter = 0                         # Counter for the currently searched number
    found = False                       # indicator for number already found
    error = False                       # Error bit

    """
    Checking algorithm
    """
    for field in range(length_whole_sudoku - 1):        # Whole verification loop
        for number in range(length_of_one_field + 1):       # Field verification loop
            found = False                                   # Reset found indicator
            for index in range(0, length_of_one_field-1):           # Current list iteration loop
                if sudo[field][index] == number and found == False:
                    found = True                                    # Mark number as found
                elif (sudo[field][index] == number and found == True) or (sudo[field][index] > length_of_one_field) or (sudo[field][index] < 0):
                    error = True                                    # Activate error bit
                    break                                           # Exit the current iteration of the list

            if error:
                break                                       # Exit verification loop of current field

        if error:
            break                                       # Exit whole verification loop

    """
    Return the result of sudoku check
    """
    if error:
        print("Sudoku has errors in it!")
    else:
        print("Sudoku has no errors!")

'''
Define test sudoku and call the check function
'''
test_sudo = [[1,2,3,4,6,6,7,8,9], [1,2,3,6,5,4,7,8,9]]
check_sudo(test_sudo)


