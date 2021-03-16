def iniContoh ():
    x = str(input('Masukkan sebuah kalimat: ini adalah sebuah CONTOH'))
    besar = x.upper
    print(besar)
    if len(x) >= 200:
        print('Batas karakter maksimal hanya 200')
    elif len(x) == 0:
        print('Masukkan sebuah inputan')
    return print(besar)
iniContoh()