# Program to print a hollow square pattern
#* * * * *
#*       *
#*       *
#*       *
#* * * * *

for i in range(5):  # Outer loop is used for rows

    
    for j in range(5):  # Inner loop is used for columns

        # Check if it is the first row, last row, first column or last column
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end=" ")         # Print star at the boundary

        else:
            print(" ", end=" ")    # Print space inside the square
    print()    # Move to the next line after each row