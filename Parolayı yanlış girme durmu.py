print("------------------KULLANICI GİRİŞİ ------------------")
sys_Kullanıcı_Adı="cemre"
sys_Parola="12345"

Kullanıcı_Adı=input("Kullanıcı Adı:")
Parola=input("Parola:")

if(Kullanıcı_Adı==sys_Kullanıcı_Adı and sys_Parola!=Parola):
    print("Parola Hatalı...")

elif(Kullanıcı_Adı!=sys_Kullanıcı_Adı and Parola==sys_Parola):
    print("Kullanıcı Adı Hatalı...")
elif(Kullanıcı_Adı!=sys_Kullanıcı_Adı and Parola!=sys_Parola):
    print("Kullanıcı Adı ve Parola Hatalı...")

else:
    print("Sisteme Başarıyla Giriş Yapıldı... ")