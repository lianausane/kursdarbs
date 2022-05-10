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
MAPE = "faili/"
fails = MAPE + "aprekini.txt"
f = open(fails, 'a', encoding="UTF-8")

print("Sveiki parbaudīsim vai vari aprēķināt dažādu figūru laukumu.")
print("Kādā apjomā veiksim darbu?")

p = 0
n = 0
apj = 0
while apjoms < 5 or apjoms > 50:
    if apjoms < 5 or apjoms > 50:
        print("Ievadīts nepareiz apjoms! Ievadi vēlreiz.")
    apjoms = int(input("Ievadi apjomu no 5 līdz 50: ")) 

print("Kādas figūras laukumu aprēķināsi?")
print("Ja taisnustūra tad ievadi 1")
print("Ja tristūra tad ievadi 2 ")
print("Ja apļa tad ievadi 3")
kf = int(input("kuru figūras laukumu apreķināsim: "))
uzd = int(input("Cik tādus uzdevumus pildi: "))
if kf = 1:
    for i in range(uzd):
    a = random.randrange(1, apjoms)
    b = random.randrange(1, apjoms)
    print(f"Kāds ir taisnustūra laukums ja tā malu garums ir šāds: {a} , {b}")
    atb = int(input("Laukums ir: "))
    if atb == a * b:
        print("Parezi!")
        p+=1
    else:
        print("Neparezi!")
        n+=1
    
    

