def numpat(n):
     
    # initialising starting number 
    num = 1
 
    # outer loop to handle number of rows
    for i in range(0, n):
     
        # re assigning num
        num = 1
     
        # inner loop to handle number of columns
            # values changing acc. to outer loop
        for j in range(0, i+1):
         
                # printing number
            if(j==i):
                print(num, end="")
            else:
                print(num, end=" ")
         
            # incrementing number at each column
            num = num + 1
     
        # ending line after each row
        if(i!=n-1):
            print()
 
# Driver code
n = int(input())
numpat(n)
