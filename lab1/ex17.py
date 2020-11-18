import time
p="1419242fe"
password=input("parolanızı girin: ")
print("Parolanızı hatırlamazsanız parolanıza ipucu yazın.")
i=0
second=5
while password != p:
  time.sleep(second*2)
  password=input("Bu parola yanlış , parolanızı girin: ")
  while password == "ipucu" and i<3:
    print(p[i])
    password=input("Bu parola yanlış , parolanızı girin: ")
    i+=1
print("Parolanız doğru hoşgeldiniz.")
print("Merhaba Fatih.")      