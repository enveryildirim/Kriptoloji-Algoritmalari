
key=[2,0,1]


def sifrele(metin):
    #sonuna x ekliyoruz metin uygun hale gelsin diye
    tmp=3-len(metin)%3
    if tmp!=0:
        for c in range(tmp):
            metin+="x"
    smetin=""
    metin=metin.lower()
    #metnimizi anahtara göre şifreliyoruz
    for c in range(0,len(metin),3):
        smetin += metin[c+key[0]]
        smetin += metin[c+key[1]]
        smetin += metin[c+key[2]]
    return smetin

def sifre_coz(metin):
    cmetin=""
    metin = metin.lower()
    i=0
    #metni 3 er 3 er gezip anahatara göre şifreyi çözüyoruz
    for c in range(0, len(metin), 3):
        cmetin += metin[key[2]+c]
        cmetin += metin[key[0]+c]
        cmetin += metin[key[1]+c]
        i=i+1
    return cmetin

def duzelt(metin):
    dmetin=""
    for c in metin:
        if c.isalpha():
            dmetin+=c
    return dmetin


sifreli_metin=sifrele(duzelt("alirıza"))
print("Şifrelenen:")
print(sifreli_metin)
print("Şifre Çözülmüşü:")
print(sifre_coz(sifreli_metin))
