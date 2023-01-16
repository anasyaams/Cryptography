import random
from math import sqrt
from random import randint as rand

#digunakan untuk mencari bilangan prima
def isprime(num):
    if num > 1:  
        for n in range(2,num):  
            if (num % n) == 0:  
                return False
        return True
    else:
        return False
      

#digunakan untuk mencari gcd dari dua bilangan
def gcd(x, y):
  if y == 0:
        return x
  else:
        return gcd(y, x % y)
    

#digunakan untuk membuat kunci (d)
def invers(totient, e):
  for x in range(1, e):
        if (totient * x) % e == 1:
            return x
  return -1


#digunakan untuk men-generate kunci
def key_generation(p, q):
  n = p*q
  totient = (p-1)*(q-1)
  arr_e = []
  for i in range(2, totient):
    if gcd(i,p-1) == 1 and invers(i, totient) != i:
      arr_e.append(i)
      
  e = random.choice(arr_e)
  d = invers(e, totient)

  return ((e, n), (d, n))


#digunakan untuk enkripsi
def enkripsi(plaintext, package):
    e, n = package
    ciphertext = pow(plaintext, e) % n

    return ciphertext
 

#digunakan untuk dekripsi  
def dekripsi(ciphertext, package):
    d, n = package
    plaintext = pow(ciphertext, d) % n
    
    return (plaintext)
  

#test
p = int(input("Nilai p : "))
if isprime(p)==False:
    print("Bilangan yang anda masukkan bukan bilangan Prima!")
    p = int(input("Nilai p (prima): "))

q = int(input("Nilai q : "))
if isprime(q)==False:
    print("Bilangan yang anda masukkan bukan bilangan Prima!")
    p = int(input("Nilai q (prima): "))

public, private = key_generation(p, q) 
print("Public Key: ", public)
print("Private Key: ", private)

pt = int(input("Plaintext: "))
ct = enkripsi(pt, public)
print("Hasil enkripsi : ")
print(ct)

print("Hasil dekripsi: ")
print(dekripsi(ct, private))


#digunakan untuk mencari plaintext dan private key jika hanya diketahui nilai public key
def attack(ciphertext, e, n):
  for i in range (2, n):
    if n % i == 0:
      p = int(n/i)
      q = int(i)

  totient = (p-1)*(q-1)
  d = invers(e, totient)
  plaintext = pow(ciphertext, d) % n

  return plaintext, d


#test
ct = int(input("Ciphertext: "))

e = int(input("Public key e : "))
n = int(input("Public key n : "))

pt, d = attack(ct, e, n)

print("Plaintext : ", pt)
print("Private key : ", d)
