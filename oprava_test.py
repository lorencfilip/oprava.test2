import random

pokracovat = True
kontrola = True
spravne = 0
spatne = 0
zivot = 2
print("Hra s poli")

while pokracovat:
       
    for i in range(random.randint(1,15)):
        pole=[]
    for i in range(random.randint(1,10)):
        pole.append(random.randint(1,50))

    print(pole)
    odpoved = int(input("Jaká je délka pole? "))
    if odpoved == len(pole):
        print("Správná odpověď")
        spravne+=1
    else:
        print("Špatá odpověď")
        spatne+=1

    if spravne<spatne:
        print("Máte hodně špatných odpovědí,odebere se vám život")
        zivot-=1
        print(f"Máte {zivot} životů")
        if zivot == 0:
            print("konec")
            break
while kontrola==True:
    odpoved = input("Chcete pokračovat? Ano nebo Ne?")
    if odpoved=="Ne":
        print("konec")
        pokracovat = False
        break
    if odpoved=="Ano":
        print("pokračujeme do nekonečna a ještě dál: ")
        pokracovat = True
        