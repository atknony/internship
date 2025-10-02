x = int(input("Asker sayısını giriniz:"))
askerler = list()

for i in range(x):
    askerler.append(i+1)

a = 1

while True:
    if len(askerler) == 1:
        break
    elif a > len(askerler):
        a = 1
    elif a == len(askerler):
        a = 0
    del askerler[a]
    a += 1                      
         
print("Sona kalan askerin numarası:",(askerler))

