for item in range(10,1,-1):
    print('')
    for item2 in range (1,item):
        print(' ',end='')
    for item3 in range(item,1,-2):
        print('',end='')
    for item4 in range(item3,1,-1):
        item4 ='*'
        print(item4,end=' ')
