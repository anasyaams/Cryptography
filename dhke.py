#mencari bilangan prima
def isprime(num):
    if num > 1:  
        for n in range(2,num):  
            if (num % n) == 0:  
                return False
        return True
    else:
        return False
      

#mencari ya, yb, dan shared key
def user():
  g = int(input("Masukkan nilai g: "))
  p = int(input("Masukkan nilai p (prima): "))
  if isprime(p)==False:
    print("Bilangan yang anda masukkan bukan bilangan Prima!")
    p = int(input("Masukkan nilai p (prima): "))
  xa = int(input("Masukkan nilai x user A: "))
  xb = int(input("Masukkan nilai x user B: "))
  ya = (pow(g, xa))%p
  yb = (pow(g, xb))%p
  print("ya: ", ya)
  print("yb: ", yb)
  ga = yb
  gb = ya
  ya = (pow(ga, xa))%p
  yb = (pow(gb, xb))%p
  print("shared key: ")
  return(ya)


#mencari xa, xb, dan shared key
def attacker():
  g = int(input("Masukkan nilai g: "))
  p = int(input("Masukkan nilai p (prima): "))
  if isprime(p)==False:
    print("Bilangan yang anda masukkan bukan bilangan Prima!")
    p = int(input("Masukkan nilai p (prima): "))
  gb = int(input("Masukkan nilai y user A: "))
  ga = int(input("Masukkan nilai y user B: "))
  for i in range(0, 10):
    if (pow(g, i))%p == gb:
      xa = i
      ya = (pow(ga, xa))%p
      print("xa: ", xa)
      print("shared key: ", ya)
      
    elif (pow(g, i))%p == ga:
      xb = i
      yb = (pow(gb, xb))%p
      print("xb: ", xb)
