def kalimat(x):
    list1 = []
    pisah = x.split()
    list1.append(pisah)
    for item in list1:
        item
        terpanjang = max(item,key=len) #nemu
        jumlah = len(terpanjang)
        print('jumlah karakter terbanyak adalah',jumlah,'karakter')
        for item2 in item:
            if len(item2) == jumlah:
                print('karakter yang berjumlah',jumlah,'adalah',item2)
x = input('Masukkan kalimat :')
kalimat(x)