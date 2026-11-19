#Question 4: Increasing Number Triangle
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5


for i in range(0,5):      #first loop for rows
    for j in range(1,i+1):  #second loop for columns
        print(j,end=" ")   #it will print i value with space 
    print()              #to new line after priniting firt rows 