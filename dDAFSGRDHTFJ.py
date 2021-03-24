assc1_number = 65
for i in range(4):
    for j in range(i + 1):
        character = chr(assc1_number)
        print(character, end=" ")
    assc1_number +=1
    print()