# Meminta input harga beli dari supplier
harga_suplier = int(input("Masukkan harga beli dari supplier: Rp. "))

# Menghitung harga jual (10% dari harga beli)
harga_jual = harga_suplier * 0.1
print(f"Harga jual setalah ditambah 10% : Rp. {int(harga_jual)}")

print(f"Total harga jual Toko: Rp. {int(harga_suplier+harga_jual)}")
