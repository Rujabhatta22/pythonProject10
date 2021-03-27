#the python code below generation 50 random even integers. Rewrite the code so it uses a while loop instead of for loop.
import random
my_list = [ ]
i=0
while i<=50:
    i+=1
    num=random.randint(1, 1200)
    if num%2==0:
        my_list.append(num)
