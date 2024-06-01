def tambah(x, y):
    x + y

def kurang(x, y):
    x - y

def kali(x, y):
    x * y

def bagi(x, y):
    if y == 0:
        print("Operasi error")
    x / y

result = 0
num = float(input("Input angka : ").format(result))
result += num

while True:
    operator = input("Pilih Operator (+, -, *, /, atau '=' untuk pengisian) : ")
    if operator == '=':
        print("Total Jumlah:", result)
        break
    
    else:
        if operator == '+':
            num_baru = float(input("Input angka selanjutnya : ".format(num)))
            result += num_baru
        elif operator == '-':
            num_baru = float(input("Input angka selanjutnya : ".format(num)))
            result -= num_baru
        elif operator == '*':
            num_baru = float(input("Input angka selanjutnya : ".format(num)))
            result *= num_baru
        elif operator == '/':
            num_baru = float(input("Input angka selanjutnya : ".format(num)))
            result /= num_baru
        else:
            print("Operator tidak sesuai")

    print("Jumlah:", result)