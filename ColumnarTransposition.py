#enkripsi
import numpy as np

def enkripsi(plaintext):

  #mencari urutan key
  alfabet = "abcdefghijklmnopqrstuvwxyz"
  no_key = list(range(len(key)))
  a = 0
  for x in range(len(alfabet)):
    for y in range(len(key)):
      if alfabet[x] == key[y]:
        a += 1 
        no_key[y] = a
  
  #membuat tabel dan mengisi sel kosong dengan huruf x
  sisa = len(plaintext) % len(key)
  total_space = len(key) - sisa
  if sisa != 0:
    for x in range(total_space):
      plaintext += "x"
  
  baris = int(len(plaintext) / len(key))
  arr = [[0] * len(key) for x in range(baris)]
  
  #mengisi tabel dg plaintext
  b = 0
  for x in range(baris):
    for y in range(len(key)):
      arr[x][y] = plaintext[b]
      b += 1
  
  #menyusun key dari yang terkecil
  lokasi_key =""
  for x in range(len(key)+1):
    for j in range(len(key)):
      if no_key[j] == x:
        lokasi_key += str(j)

  #menentukan ciphertext
  ciphertext = ""
  c = 0
  row = baris*2
  for x in range(row):
    d = int(lokasi_key[c])
    for y in range(baris):
      ciphertext += arr[y][d]
    c += 1
    if c == len(key):
      break
  #print(np.matrix(arr))

  return ciphertext

#main
key = input('Masukkan key: ').lower()
plaintext = input('Masukkan Plain Text: ').replace(" ", "")
ciphertext = enkripsi(plaintext)

print("Cipher Text: ", ciphertext)




#dekripsi
def dekripsi(ciphertext):

  #mencari urutan key
  alfabet = "abcdefghijklmnopqrstuvwxyz"
  no_key = list(range(len(key)))
  a = 0
  for x in range(len(alfabet)):
    for y in range(len(key)):
      if alfabet[x] == key[y]:
        a += 1 
        no_key[y] = a

  #membuat tabel
  baris = int(len(ciphertext) / len(key))
  arr = [[x] * len(key) for x in range(baris)]

  #menyusun key dari yang terkecil
  lokasi_key =""
  for x in range(len(key)+1):
    for j in range(len(key)):
      if no_key[j] == x:
        lokasi_key += str(j)
  
  #mengisi tabel dg ciphertext 
  a, j = 0, 0
  for x in range(len(ciphertext)):
    b = 0
    if a == len(key):
      a = 0
    else:
      b = int(lokasi_key[a])
    for y in range(baris):
      arr[y][b] = ciphertext[j]
      j += 1
    if j == len(ciphertext):
      break
    a += 1
  #print(np.matrix(arr))
  
  #menentukan plaintext
  plaintext = ""
  for x in range(baris):
    for y in range(len(key)):
      plaintext += str(arr[x][y])

  return plaintext

#main
key = input('Masukkan key: ').lower()
ciphertext = input('Masukkan Chiper Text: ').replace(" ", "")
plaintext = dekripsi(ciphertext)

print("Plain Text: ", plaintext)
