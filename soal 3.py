x = [1,3,2,2,1,5,1,24,12,124,12,21,32,15]

def sort_odd_even(x):
    genap = []
    ganjil = []
    for item in x:
        if item % 2 == 0:
            genap.append(item)
        else:
            ganjil.append(item)
    urutGenap = sorted(genap)
    urutGanjil = sorted(ganjil)
    return urutGanjil+urutGenap
print(sort_odd_even(x))