#Question 11: Hollow Right-Angled Triangle
#*
#* *
#*   *
#*     *
#* * * * *



for i in range(5):          # Rows
    for j in range(5):      # Columns
        if j == 0 or i == j or i == 4:
            print("*", end=" ")  # Print star in the first column
        else:
            print(" ", end="")
    print()