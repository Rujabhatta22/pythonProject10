ascii_number = ord('A')
for i in range(6,1,-1):
    for j in range( 1, i-1):
        character = chr(ascii_number)
        print(character, end=" ")
        ascii_number +=1
    print()