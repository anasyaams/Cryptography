#enkripsi
def enkripsi(plaintext, keyword):
  tabel_adfgvx = "8p3d1nlt4oah7kbc5zju6wgmxsvir29ey0fq"
  adfgvx = 'ADFGVX'

  #memasukkan keyword ke dalam array key
  key = []
  for c in keyword:
      key.append(c)

  #mengurutkan key
  n_key = len(key)
  sorted_key = sorted(range(n_key), key=lambda i: key[i])

  #menentukan ciphertext
  ciphertext = []
  for c in plaintext.lower():
    if c.isalpha() or c.isdigit():
      row, col = divmod(tabel_adfgvx.index(c), 6)
      ciphertext += [adfgvx[row], adfgvx[col]]

  #mengurutkan ciphertext berdasarkan key
  return ''.join(ciphertext[j] for i in sorted_key for j in range(i, len(ciphertext), n_key))

#main
keyword = input('Masukkan key: ')
plaintext = input('Masukkan Plain Text: ')
print ("Ciphertext : {}".format(enkripsi(plaintext, keyword)))




#dekripsi
def dekripsi(ciphertext, keyword):
  tabel_adfgvx = "8p3d1nlt4oah7kbc5zju6wgmxsvir29ey0fq"
  adfgvx = 'ADFGVX'

  #memasukkan keyword ke dalam array key
  key = []
  for c in keyword:
      key.append(c)
  
  #mengurutkan key
  n_key = len(key)
  sorted_key = sorted(range(n_key), key=lambda i: key[i])

  #mengurutkan ciphertext 
  m = len(ciphertext)
  x = [j for i in sorted_key for j in range(i, m, n_key)]

  #reorder
  y = ['']*m
  for i, c in zip(x, ciphertext):
    y[i] = c

  #menentukan plaintext
  plaintext = []
  for i in range(0, m, 2):
      row, col = y[i:i+2]
      plaintext.append(tabel_adfgvx[6 * adfgvx.index(row) + adfgvx.index(col)])
  return ''.join(plaintext)

#main
keyword = input('Masukkan key: ')
ciphertext = input('Masukkan Cipher Text: ')
print ("Plain Text : {}".format(dekripsi(ciphertext, keyword)))
