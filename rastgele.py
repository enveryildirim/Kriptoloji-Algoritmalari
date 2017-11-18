import sys
#şifreleme
Liste1 = dict(zip("abcçdefgğhıijklmnoöprsştuüvyz",range(29)))
Liste4 = dict(zip(range(29),"ertyuıopğüişlkjhgfdsazcvbnmöç"))
#çözme
Liste2 = dict(zip("ertyuıopğüişlkjhgfdsazcvbnmöç",range(29)))
Liste3 = dict(zip(range(29),"abcçdefgğhıijklmnoöprsştuüvyz"))




def Sifrele(metin):
    smetin = ""
    for c in metin.lower():
        #şifrelenecek karakter birinci dizinden indisi bulunup şifreli dördüncü  diziden karaşılığı bulunup metne ekleniyor
        if c.isalpha(): smetin += Liste4[Liste1[c]]

    print("Sifrelendi:"+smetin)

def SifreCoz(metin):
    cmetin= ""
    for c in metin.lower():
        # şifresi çözülecek karakter ikinci dizinden indisi bulunup normal olan üçüncü  diziden karaşılığı bulunup metne ekleniyor
        if c.isalpha(): cmetin += Liste3[Liste2[c]]

    print("Cözüldü:"+cmetin)

argumanlar = sys.argv
if argumanlar[1]=="-sifrele":
    a=input("Lütfen Metni Giriniz :")
    Sifrele(a)

if argumanlar[1]=="-coz":
    a = input("Lütfen Metni Giriniz :")
    SifreCoz(a)


