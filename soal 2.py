a = list(map(int, input("Masukkan nomor telepon: ").split()))
print(len(a))
if len(a) >= 13:
    print('nomor HP hanya maksimal 13 angka')