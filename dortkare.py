import sys
#matrisleri tanımlıyoruz
matris1 = [['a', 'b', 'c','ç', 'd'],
          ['e', 'f', 'g', 'ğ', 'h'],
          ['ı', 'i', 'j', 'k', 'l'],
          ['m', 'n', 'o', 'ö', 'p'],
          ['r', 's', 'ş', 't', 'u'],
          ['ü', 'v', 'y', 'z', 'x']]

matris2 = [['a', 'b', 'c','ç', 'd'],
          ['e', 'f', 'g', 'ğ', 'h'],
          ['ı', 'i', 'j', 'k', 'l'],
          ['m', 'n', 'o', 'ö', 'p'],
          ['r', 's', 'ş', 't', 'u'],
          ['ü', 'v', 'y', 'z', 'x']]

#rastgele değerler elle giriliyor
matris3 = [['e', 's', 'd','l', 'ç'],
          ['r', 'a', 'f', 'ş', 'ö'],
          ['t', 'ü', 'g', 'i', 'm'],
          ['y', 'ğ', 'h', 'z', 'n'],
          ['u', 'p', 'j', 'c', 'b'],
          ['ı', 'o', 'k', 'x', 'v']]


matris4 = [['x', 'i', 'ş','c', 'v'],
          ['e', 'ü', 'l', 'z', 'b'],
          ['r', 'ğ', 'k', 'a', 'n'],
          ['t', 'p', 'j', 's', 'm'],
          ['y', 'o', 'h', 'd', 'ö'],
          ['u', 'ı', 'g', 'f', 'ç']]

#bu fofnksiyon istediğimiz matristen istedeğimiz harfin koordinatı verecek
def IndexKac(harf,matris):
    for x in range(len(matris)):

        for y in range(len(matris[x])):
            if matris[x][y] == harf:
                return [x,y]

#Şifreleem
def Sifrele(metin):
    smetin="";
    #şifrelenecek metni ikişer ikişer geziyoruz
    for c in range(0,len(metin),2):
            #birinci harfin koordinatını buluyoruz
            x=IndexKac(metin[c],matris1)
            # ikinci harfin koordinatını buluyoruz
            y=IndexKac(metin[c+1],matris2)
            #birinci harfin satırıyla ikinci harfin sütünü 3.matriste denk harfi buluyoruz
            smetin+=matris3[x[0]][y[1]]
            # ikinci harfin satırıyla birinci harfin sütünü 4.matriste denk harfi buluyoruz
            smetin+=matris4[y[0]][x[1]]


    print(smetin)

#Şifre Çözme
def SifreCoz(metin):
    cmetin=""
    #şifrelenmiş metni ikişer ikişer geziyoruz
    for c in range(0, len(metin), 2):

        # birinci harfin koordinatını buluyoruz
        x = IndexKac(metin[c], matris3)
        # ikinci harfin koordinatını buluyoruz
        y = IndexKac(metin[c + 1], matris4)
        # birinci harfin satırıyla ikinci harfin sütünü 3.matriste denk harfi buluyoruz
        cmetin += matris1[x[0]][y[1]]
        # ikinci harfin satırıyla birinci harfin sütünü 4.matriste denk harfi buluyoruz
        cmetin += matris2[y[0]][x[1]]
    #bazı durumlar için koyduğumuz x çıkartıp yazdırıyoruz
    print(cmetin.replace("x",""))

#metinin içindeki boşluk ve karakterleri çıkaran fonksiyon
def Duzelt(metin):
    tmp=""
    for c in metin.lower():
        if c.isalpha():tmp+=c
    return tmp
#girilen karakter sayısı tek ise sonu x ekleyip çift yapan fonksiyon
def Tek(metin):
    if len(metin)%2!=0:
        metin+="x";
    return metin


argumanlar = sys.argv
if argumanlar[1]=="-sifrele":
    a=input("Lütfen Metni Giriniz :")
    a=Duzelt(a)
    Sifrele(Tek(a))

if argumanlar[1]=="-coz":
    a = input("Lütfen Metni Giriniz :")
    a=Duzelt(a)
    SifreCoz(Tek(a))