# Butterfly pattern
#*                 *
#* *             * *
#* * *         * * *
#* * * *     * * * *
#* * * * * * * * * *
#* * * *     * * * *
#* * *         * * *
#* *             * *
#*                 *



n = 5

# Upper half
for i in range(1, n + 1):   # Loop for rows
    for j in range(1, i + 1):   # Print left stars
        print("*", end=" ")
    for j in range(1, 2 * (n - i) + 1):  # Print middle spaces
        print(" ", end=" ")
    for j in range(1, i + 1):   # Print right stars
        print("*", end=" ")
    print()    # Move to next line

# Lower half
for i in range(n - 1, 0, -1):   # Loop in reverse order
    for j in range(1, i + 1):   # Print left stars
        print("*", end=" ")
    for j in range(1, 2 * (n - i) + 1):   # Print middle spaces
        print(" ", end=" ")
    for j in range(1, i + 1):   # Print right stars
        print("*", end=" ")
    print()