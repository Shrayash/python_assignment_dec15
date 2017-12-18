a=input('enter your name:')
firstname=a.strip().split(' ')[0]
print('firstname:{}'.format(firstname))
name=a.strip().split(' ')
if(len(name)==3):
    middlename=name[1]
    print('middlename:{}'.format(middlename))
    lastname=name[2]
    print('lastname:{}'.format(lastname))
else:
    lastname=name[1]
    print('lastname:{}'.format(lastname))


