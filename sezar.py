import sys

#alfabemiz
Liste1 = dict(zip("abcçdefgğhıijklmnoöprsştuüvyz",range(29)))
Liste2 = dict(zip(range(29),"abcçdefgğhıijklmnoöprsştuüvyz"))
#kaydırma miktarı
key = 3
#şifreleme
def Sifrele(metin):
    smetin = ""
    #metin karakter karakter geziliyor ve küçük harf yapıyoruz
    for c in metin.lower():
        # if kontrolü ise boşluk ve işaret önüne geçiyoruz harf ise işlem yapıyor
        if c.isalpha():
            #birinci dizideki harfin indeksi alıp 3 karakter kaydırıp, herhangi bir taşmayı engellemekiçin  mod 29 alıyoruz
            smetin += Liste2[ (Liste1[c] + key)%29 ]

    print("Sifrelendi:"+smetin)

def SifreCoz(metin):
    cmetin= ""
    for c in metin.lower():
        # birinci dizideki harfin indeksi alıp 3 karakter azaltıp, herhangi bir taşmayı engellemekiçin  mod 29 alıyoruz
        if c.isalpha(): cmetin += Liste2[ (Liste1[c] - key)%29 ]

    print("Cözüldü:"+cmetin)


argumanlar = sys.argv
if argumanlar[1]=="-sifrele":
    a=input("Lütfen Metni Giriniz :")
    Sifrele(a)

if argumanlar[1]=="-coz":
    a = input("Lütfen Metni Giriniz :")
    SifreCoz(a)


