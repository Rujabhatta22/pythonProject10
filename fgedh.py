#what will be the output of following program? Rewrite the code using for loop to display same output.
n=6
i=0
for i in range(n):
    i+=1
    if i==3:
        continue
    print(i)
