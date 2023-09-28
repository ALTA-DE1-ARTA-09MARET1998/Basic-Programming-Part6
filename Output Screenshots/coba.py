def ArrayUnique(arr1, arr2):
    # Mengkonversi arr2 menjadi set untuk menghapus duplikasi
    set_arr2 = set(arr2)
    
    # Membuat array hasil yang awalnya kosong
    result = []

    # Iterasi melalui elemen-elemen arr1
    for num in arr1:
        # Jika elemen num tidak ada di set_arr2, tambahkan ke hasil
        if num not in set_arr2:
            result.append(num)

    return result

# Contoh penggunaan:
arr1 = [1, 2, 3, 4]
arr2 = [1, 3, 5, 10, 16]
hasil = ArrayUnique(arr1, arr2)
print("Array hasil:", hasil)