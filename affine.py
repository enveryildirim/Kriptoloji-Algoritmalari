#alfabemiz
Liste1 = dict(zip("abcçdefgğhıijklmnoöprsştuüvyz",range(29)))
Liste2 = dict(zip(range(29),"abcçdefgğhıijklmnoöprsştuüvyz"))

#doğrusal fonksiyon değerleri
a=5
b=2

def sifrele(metin):
    smetin=""
    for c in metin.lower():
        smetin+=sifre_formul(Liste1[c])
    return smetin

def sifre_formul(sayi):
    #fonksiyonu uygulayıp şifreli değeri buluyoruz
    tmp=((a*(sayi))+b)%29

    return Liste2[tmp]


def sifre_coz_formul(harf):
    tmp=0
    #a'nın a' bluyoruz
    z=0
    for c in range(29):
        if (c*a)%29==1:
            z=c
            break
    #şifre çözme fonksiyonu uygulayarak çözülmüş değeri buluyoruz
    tmp=z*(Liste1[harf]-b)%29

    return Liste2[tmp]

def sifre_coz(metin):
    cmetin=""
    for c in metin.lower():
        cmetin+=sifre_coz_formul(c)
    return cmetin

print("Şifrelenen:")
sifreli_metin=sifrele("haydar")
print(sifreli_metin)
print("Şifre Çözülmüşü:")
cozulmus_metin=sifre_coz(sifreli_metin)
print(cozulmus_metin)