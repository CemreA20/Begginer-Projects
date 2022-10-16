import random
secenek=["Taş","Kağıt","Makas"]

print("Taş,Kağıt, Makas Oyununa Hoş Geldiniz ")
while True:
    secim = input("Taş mı Kağıt mı Makas mı? ")
    a_secim = random.choice(secenek)

    if secim=="Taş":
        if a_secim=="Taş":
            print("Bilgisayarın seçimi:Taş  Sonuç:Berabere...")
        elif a_secim=="Kağıt":
            print("Bilgisayarın seçimi Kağıt,bilgisayar Kazandı")
        else:
            print("Bilgisayarın Seçimi Makas,tebrikler Kazandınız!")

    if secim=="Kağıt":
        if a_secim== "Kağıt":
            print("Bilgisayarın Şeçimi:Kağıt  Sonuç:Berabere...")
        elif a_secim=="Makas":
            print("Bilgisayarın Seçimi Makas ,bilgisayar Kazandı")
        else:
            print("Bilgisayarın Seçimi Taş,tebrikler Kazandınız!")

    if secim=="Makas":
        if a_secim=="Makas":
            print("Bilgisayarın Seçimi:Makas  Sonuç:Berabere...")
        elif a_secim=="Taş":
            print("Bilgisayarın Seçimi Taş,bigisayar kazandı")
        else:
            print("Bilgisayarın Seçimi Kağıt,Tebrikler Kazandınız!")
