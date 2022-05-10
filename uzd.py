"""
1. Aprekināt taisnstūra laukumu ja malu garumus izvada dators
2.Aprekināt tristūra  laukumu ja malu garumus un augstumu  izvada dators
3. aprēķinat apļa laukuma ja dots radius
4. Datu apjomu pajautās lietotājam. 
Programma pārbaudīs vai lietotājs ir ievadījis pareizi apjomu.
skaitīt pareizās atbildes 
pajautāt cik reizes šadas darbibas pildīs
"""
import random
import math
MAPE = "faili/"
fails = MAPE + "aprekini.txt"
f = open(fails, 'a', encoding="UTF-8")

print("Sveiki parbaudīsim vai vari aprēķināt dažādu figūru laukumu.")
print("Kādā apjomā veiksim darbu?")

p = 0
n = 0
apj = 0
while apj < 5 or apj > 50:
    if apj < 5 or apj > 50:
        print("Ievadīts nepareiz apjoms! Ievadi vēlreiz.")
    apj = int(input("Ievadi apjomu no 5 līdz 50: ")) 

print("Kādas figūras laukumu aprēķināsi?")
print("Ja taisnustūra tad ievadi 1")
print("Ja tristūra tad ievadi 2 ")
print("Ja apļa tad ievadi 3")
kf = int(input("kuru figūras laukumu apreķināsim: "))
uzd = int(input("Cik tādus uzdevumus pildi: "))
if kf == 1:
    for i in range(uzd):
        a = random.randrange(1, apj)
        b = random.randrange(1, apj)
        print(f"Kāds ir taisnustūra laukums ja tā malu garums ir šāds: {a} , {b}")
        atb = int(input("Laukums ir: "))
        if atb == a * b:
            print("Parezi!")
            p+=1
        else:
            print("Neparezi!")
            n+=1
    print(f"No {uzd} piemēriem pareizi bija {p} uzdevumi un nepareizs {n}. Kopumā sekmīgi tika veikti {p*100/uzd}%")            
elif kf == 2:
    for i in range(uzd):
        c = random.randrange(1, apj)
        d = random.randrange(1, apj)
        print(f"Kāds ir laukums tristūrim ja tā malas garums ir {c} un augstums pret to malu ir {d}")
        atb =int(input("Laukums ir: "))
        if atb == c*d/2:
            print("Parezi!")
            p+=1
        else:
            print("Neparezi!")
            n+=1
    print(f"No {uzd} piemēriem pareizi bija {p} uzdevumi un nepareizs {n}. Kopumā sekmīgi tika veikti {p*100/uzd}%")
elif kf == 3:
    for i in range(uzd):
        e = random.randrange(1, apj)
        print(f"Kāds ir apļa laukums, ja tā radius ir {e} pi vertību ņem kā 3.14")
        atb =float(input("Laukums ir: "))
        if atb == e*e*3.14:
            print("Parezi!")
            p+=1
        else:
            print("Neparezi!")
            n+=1
    print(f"No {uzd} piemēriem pareizi bija {p} uzdevumi un nepareizs {n}. Kopumā sekmīgi tika veikti {p*100/uzd}%")
            

    



    

