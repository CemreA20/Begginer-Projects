print(""""*****************************
ATM MAKİNASINA HOŞHGELDİNİZ.
İşlemler;
1.Bakiye Sorgulama

2.Para Yatırma

3.Para Çekme

Programdan çıkmak için 'q' ya basın.
*********************************
""")

Bakiye=1000
while True:
    işlem=input("İşlem Seçiniz:")
    if (işlem=="q"):
       print ("Yine Bekleriz...")
       break


    elif (işlem=="1"):
         print("Bakiyeniz {} tl dir.".format(Bakiye))


    elif (işlem=="2"):
         miktar =int(input("Miktarı Giriniz:"))
         print("Bakiyenize " +str(miktar)+ " tl yatırılmıştır.")
         Bakiye+=miktar


    elif (işlem=="3"):
        miktar=int(input("Miktarı Giriniz:"))
        print("Lütfen bankamatikten paranızı alın.")


        if(Bakiye-miktar<0):
            print("Bu miktarı çekemezsiniz.")
            continue
        Bakiye-=miktar
    else:
        print("Geçersiz İşlem...")
