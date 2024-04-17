# Meminta input harga beli dari supplier
harga_supplier = float(input("Masukkan harga beli dari supplier: Rp. "))

# Menghitung harga jual (10% dari harga beli)
harga_jual = harga_supplier * 0.1
print(f"Harga jual setelah ditambah 10%: Rp. {int(harga_jual)}")

# Menghitung total harga jual di toko
total_harga_jual = harga_supplier + harga_jual
print(f"Total harga jual Toko: Rp. {int(total_harga_jual)}")

# Menghitung modal dan laba
modal = harga_supplier
laba = harga_jual

print(f"Modal yang dikeluarkan: Rp. {int(modal)}")
print(f"Laba yang didapat: Rp. {int(laba)}")
