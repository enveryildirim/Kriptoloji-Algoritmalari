
#alfabemiz
Liste1 = dict(zip("abcçdefgğhıijklmnoöprsştuüvyz",range(29)))
Liste2 = dict(zip(range(29),"abcçdefgğhıijklmnoöprsştuüvyz"))

key="ali"
def duzelt(metin):
    dmetin=""
    for c in metin.lower():
        if c.isalpha():
            dmetin+=c
    return dmetin

def sifrele(metin):
    #metni 3 er 3 er bölüyor
    tmp = 3 - len(metin) % 3
    if tmp != 0:
        for c in range(tmp):
            metin += "j"
    smetin=""
    i=0

    for c in metin:
        smetin+=sifrele_formul(c,i)
        i=i+1
    return smetin

#şifreleme fonksiyon
def sifrele_formul(harf,sayi):
    #harfin değerini buluyorz
    a=Liste1[harf]
    #Anahtarımızın değerini buluyoruz
    b=Liste1[key[sayi%3]]
    #değerleri toplayıp modu alarak şifrelenmiş karakterin değerini buluyoruz
    tmp=(a+b)%29
    #şifreli karakteri listeden bulup gönderiyoruz
    return Liste2[tmp]

def sifre_coz(metin):
    cmetin=""
    i=0
    for c in metin:
        cmetin+=sifre_coz_formul(c,i)
        i=i+1
    return cmetin

#şifre çözme fonksiyonu
def sifre_coz_formul(harf,sayi):
    a=Liste1[harf]
    b=Liste1[key[sayi%3]]
    #Şifrelenenmiş değeri bulmak için çıkartıyoruz
    tmp=(a-b)%29
    #şifre çözülmüş karakteri listeden bulup gönderiyoruz
    return Liste2[tmp]


sifreli_metin=sifrele("enver")
print("Şifrelenen:")
print(sifreli_metin)
cozulmus_metin=sifre_coz(sifreli_metin)
print("Şifre Çözülmüşü:")
print(cozulmus_metin)