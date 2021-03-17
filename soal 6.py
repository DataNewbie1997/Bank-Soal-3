list1 = list([4,7,10])
list2 = list([2,6,18])
def AP (x):
    for item in list1:
        print(item, end = ' ')
    return print('\n'+'AP',item + 3)
AP(list1)
def GP (x):
    for item2 in list2:
        print(item2, end =' ')
    return print('\n'+'GP',item2 * 3)
GP(list2)