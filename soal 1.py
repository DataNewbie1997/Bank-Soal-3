def iniContoh ():
    x = str(input('Masukkan sebuah kalimat: ini adalah sebuah CONTOH :'))
    x2 = x.upper()
    if len(x2) >= 200:
        return print('Batas karakter maksimal hanya 200')
    elif len(x2) == 0:
        print('Masukkan sebuah inputan')
    return print(x2)
iniContoh()
