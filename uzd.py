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

apj = 0
while apjoms < 5 or apjoms > 50:
    if apjoms < 5 or apjoms > 50:
        print("Ievadīts nepareiz apjoms! Ievadi vēlreiz.")
    apjoms = int(input("Ievadi apjomu no 5 līdz 50: ")) 

print("Kādu figūru laukumu aprēķināsi?")

