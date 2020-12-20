("Bu örnekte Python ile kullanıcının girdiği sayıyı İkilik Sayı Sistemine çevireceğiz.")


decimal = int(input("bir decimal sayı giriniz"))
binary = bin(int(decimal)).replace("0b","")
print("Binary:",binary)
