import random

harf="QWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇqwertyuıopğüasdfghjklşizxcvbnmöç"
sayi="1234567890"
işaret="+-/*!&$#?=@"
sifre=int(input("Parolanız kaç haneli olsun"))
parola=""

for i in range(sifre):
    if i % 3==0:
        rastgele_harf=random.choice(harf)
        parola +=rastgele_harf
    elif i % 3==1:
        rastgele_sayi=random.choice(sayi)
        parola +=rastgele_sayi
    else:
        rastgele_işaret=random.choice(işaret)
        parola +=rastgele_işaret
print(parola)
