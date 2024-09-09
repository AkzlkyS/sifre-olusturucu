import random
karakter="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sayi=int(input("parolanız kaç haneli olsun:"))
parola=""

for i in range(sayi):
    parola += random.choice(karakter)
print(parola)
