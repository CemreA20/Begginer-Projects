print ("**********KULLANICI GRİŞİ**********")
sys_Kullanıcı_Adı="Cemre"
sys_Parola="12345"
giriş_hakkı=3

while True:
    Kullanıcı_Adı= input("Kullanıcı Adı:")
    Parola=input("Parola:")
    if (giriş_hakkı==0):
        print("Giriş Hakkınız Kalmadı...")
        break

    elif (Kullanıcı_Adı == sys_Kullanıcı_Adı and sys_Parola != Parola and giriş_hakkı!=0):
        print("Parola Hatalı...")
        giriş_hakkı -= 1
    elif (Kullanıcı_Adı != sys_Kullanıcı_Adı and Parola == sys_Parola and giriş_hakkı!=0 ):
        print("Kullanıcı Adı Hatalı...")
        giriş_hakkı -= 1
    elif (Kullanıcı_Adı != sys_Kullanıcı_Adı and Parola != sys_Parola and giriş_hakkı!=0):
        print("Kullanıcı Adı ve Parola Hatalı...")
        giriş_hakkı -= 1
    else:
        print("Sisteme Başarıyla Giriş Yapıldı...")
        break