

'''
uzatılmış öklidi fonksiyonu ile d hesalıyoruz
Bir sayı hangi sayı ile çarpılırsa totient fonk değerinin modu 1 olur
d*e=1modT
'''
def u_oklid(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = u_oklid(b % a, a)
        return (g, x - (b // a) * y, y)

'''
en büyük ortak bölen
'''
def obeb(a, b):
    while b != 0:
        a, b = b, a % b
    return a

'''
numaranın asal sayı olup olmadığı kontrol ediyoruz
'''
def asal_mi(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


def anahtar_olustur():

    #1.adım  p ve q değeri veriyoruz 
    p,q=61,53
    
    #2.Adım n değerini buluyoruz
    n = p*q

    #Adım 3 totient fonksiyonu  hesaplıyoruz
    '''phi(n) = phi(p)*phi(q)
        totient fonksiyonu
    '''
    toti = (p-1) * (q-1) 
    print("totient fonksiyonu ",toti)
    
    #Adım 4 e yi bulma
    '''totient fonk>e>1 ve totient ile aralarında asal bir sayı seçiyoruz'''    
    e = 151
   
    '''
    Yani basitçe de = 1 mod toti denklemini bilinen bir d ve p sayısı için çözmektir. 
    Başka bir ifadeyle bir sayının bir modda hangi sayıyla çarpılınca 1 sonucunu verdiğini bulmaktır.
    '''
    d = u_oklid(e, toti)[1]
    
    '''d nin negatif ise onu pozitif yapıyoruz'''
    d = d % toti
    if(d < 0):
        d += toti
    #private ve public key olarak gönderiyoruz    
    return ((e,n),(d,n))
        
def sifre_coz(ctext,private_key):
    '''
     m = c^d mod n
    '''
    try:
        key,n = private_key
        text = [chr(pow(char,key,n)) for char in ctext]
        return "".join(text)
    except TypeError as e:
        print(e)

def sifrele(text,public_key):
    '''
    c = m^e mod n
    '''
    key,n = public_key
    ctext = [pow(ord(char),key,n) for char in text]
    return ctext

if __name__ == '__main__':
    
    #anahtarları ayarlıyoruz
    public_key,private_key = anahtar_olustur() 
    print("Public Anahtar: ",public_key)
    print("Private Anahtar: ",private_key)
    
    smetin = sifrele("enver",public_key)
    print("Şifrelenmiş  =",smetin)
    print(smetin)
    cmetin = sifre_coz(smetin, private_key)
    print("Çözülmüş  =",cmetin)
  