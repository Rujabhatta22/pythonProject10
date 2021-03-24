time=int(input('enter the time'))
if time>0 and time<12:
    print('it is am')
elif time>12 and time<24:
    print('it is pm')