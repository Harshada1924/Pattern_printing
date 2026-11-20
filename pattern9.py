#Question 9: Diamond
#        *
#      * * *
#    * * * * *
#  * * * * * * *
#* * * * * * * * *
#  * * * * * * *
#    * * * * *
#      * * *
#        *


n=5
for i in range(1,n):    #loop for rows
    for j in range(n-i):   # loop to print first spaces
        print(" ",end="")  #print space
    for k in range(2*i-1):     #loop to print star
        print("*",end="")   #print star
        
    print()
for i in range(n,0,-1):    #loop for rows
    for j in range(n-i):   # loop to print first spaces
        print(" ",end="")  #print space
    for k in range(2*i-1):     #loop to print star
        print("*",end="")   #print star
        
    print()