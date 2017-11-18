import sys

#alfabemiz
Liste1 = dict(zip("abcçdefgğhıijklmnoöprsştuüvyz",range(29)))
Liste2 = dict(zip(range(29),"abcçdefgğhıijklmnoöprsştuüvyz"))

print("kaydırma katsayısı girmeyi unutmayın")
argumanlar = sys.argv
#kaydırma miktarı
key = int(argumanlar[2])

def Sifrele(metin):
    smetin = ""
    for c in metin.lower():
        if c.isalpha():
            # birinci dizideki harfin indeksi alıp kaydırma miktarı karakter kaydırıp, herhangi bir taşmayı engellemekiçin  mod 29 alıyoruz
            smetin += Liste2[ (Liste1[c] + key)%29 ]

    print("Sifrelendi:"+smetin)

def SifreCoz(metin):
    cmetin= ""
    for c in metin.lower():
        if c.isalpha():
            # birinci dizideki harfin indeksi alıp kaydırma miktarı kadar karakter azaltıp, herhangi bir taşmayı engellemekiçin  mod 29 alıyoruz
            cmetin += Liste2[ (Liste1[c] - key)%29 ]

    print("Cözüldü:"+cmetin)



if argumanlar[1]=="-sifrele":
    a=input("Lütfen Metni Giriniz :")
    Sifrele(a)

if argumanlar[1]=="-coz":
    a = input("Lütfen Metni Giriniz :")
    SifreCoz(a)


