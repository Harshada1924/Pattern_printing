#Question 7: Star Pyramid
#        *
#      * * *
#    * * * * *
#  * * * * * * *
#* * * * * * * * *

n=5
for i in range(1,n+1):    #loop for rows
    for j in range(n-i):   # loop to print first spaces
        print(" ",end="")  #print space
    for k in range(2*i-1):     #loop to print star
        print("*",end="")   #print star
        
    print()