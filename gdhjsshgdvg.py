#write a program to check a number given by the user is armstrong or not.
num=int(input("enter the number:"))
t= num
sum=0
while num>0:
    rem = num % 10
    sum = sum + rem**3
    num = num // 10
print(sum)
if sum==t:
    print('armstrong')
else:
    print('not armstrong')