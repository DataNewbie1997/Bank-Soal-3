def nomorHP (x):
    if len(x) >= 13:
        print('Nomor HP maksimal 13 angka')
    else:
        if (x[0:2]) != '08':
            print('Nomor HP harus dimulai dengan "08"')
        else: 
            print('Nomor HP saya adalah',x)
x = input('masukkan nomor HP:')
nomorHP(x)
