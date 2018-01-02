# coding: utf-8

import numpy as np

def matris_ayarla():
    #rastgele matris oluşturuyoruz
    input_key = input("Matris boyut giriniz: ")
    i_key = []
    for ch in input_key:
        if ch.isalnum():
            i_key += [ord(ch)]   
                     
    all_cell = len(i_key)
    row_cell = int(all_cell**0.5)
    key_matrix = []
    
    if (row_cell*row_cell) != all_cell:
        print("Lütfen a x a gibi bir matris giriniz ")
        return matris_ayarla()
    else:
        for i in range(0,all_cell,row_cell):
            key_matrix += [i_key[i:i+row_cell]]
    key_matrix = np.mat(key_matrix,dtype = int)
    
    
    return key_matrix

#yazıyı matris çeviren fonksiyon
def yazı_to_matris(p_text,size):
   
    p_text = [ord(c) for c in p_text]
    
    text_matrix = []
    while len(p_text) > size:
        piece = p_text[:size]
        text_matrix.append(piece)
        p_text = p_text[size:]
    text_matrix.append(p_text)
    
    try:
        text_matrix = np.mat(text_matrix, dtype=int)
    
    except Exception:
        
        p_text_again = input("Metin giriniz: \n")
        
        return yazı_to_matris(p_text_again, size)
   
    return text_matrix
        
def sifrele(plain_text, key):
    #matrisin şifre matrisi ile çarpıyoruz
    cipher_text = np.matmul(plain_text, key)
    arr = ""
    for i in np.array(cipher_text).flat:
        arr += chr(i % 26 + ord('a'))
    print("\nşifreli metin:\n",arr)
    return cipher_text


def sifre_coz(cipher_text, key):
   #matrisin tersini alıp
    try:
        inv_key = np.linalg.inv(key) 
    except Exception:   
        quit()
         
    decrypted_text = np.matmul(cipher_text, inv_key)
    arr = ""
	
    for i in decrypted_text.flat:
        arr += chr(int(round(i)))
    
    print("çözülmüş metin:\n",arr)
    
    return decrypted_text
   
   
if __name__ == '__main__':

    key = np.mat(matris_ayarla(), dtype=int)
    
    p_text = input("şifrelenecek metin: ")
    row_length = len(key)
    metin_matris = yazı_to_matris(p_text, row_length)

    smetin = sifrele(metin_matris, key)
    print("şifrelenmiş :", smetin) 

    cmetin = sifre_coz(smetin, key)
    print("çözülmüş :", cmetin)
