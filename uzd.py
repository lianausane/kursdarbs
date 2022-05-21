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

print()
print("Sveiki parbaudīsim vai vari aprēķināt dažādu figūru laukumu.")
print("Kādā apjomā veiksim darbu?")
print( )
p = 0
n = 0
apj = 0
while apj < 5 or apj > 50:
    if apj < 5 or apj > 50:
        print("Ievadīts nepareiz apjoms! Ievadi vēlreiz.")
    apj = int(input("Ievadi apjomu no 5 līdz 50: ")) 

rows, cols =(10,10)
arr=[]
for i in range(rows):
    col=[]
    for j in range(cols):
        col.append((i+1)*(j+1))
    arr.append(col)

print("Reizrēķina tabula sakrīt ar taisnustūru laukumu rezultātiem tādēļ varbūt noderēs šī tabula:")  
for i in range(rows):
    for j in range(cols):
        print(arr[i][j], end="\t")
    print()  

print("Kādas figūras aprēķināsi?")
print("Ja taisnustūra laukumu tad ievadi 1")
print("Ja tristūra laukumu tad ievadi 2 ")
print("Ja apļa laukumu tad ievadi 3")
print("Ja taisnustūra perimetru tad ievadi 4")
print("Ja tristūra perimetu tad ievadi 5 ")
print("Ja apļa diametru tad ievadi 6")
print("Ja riņķa līnijas garumu tad ievadi 7")
print("Ja trapeces laukumu tad ievadi 8")
o = 0
t = 0
while o == t:
    kf = int(input("kuru figūras funkciju apreķināsim: "))
    f.write("kuru figūras funkciju apreķināsim: " + "\n")
    uzd = int(input("Cik tādus uzdevumus pildi: "))
    f.write("Cik tādus uzdevumus pildi: " + "\n")
    try:
        print(uzd)  
    except: 
        print("Mainīgais kuru mēģinat izvadīt nav definēts!")
        f.write("Mainīgais kuru mēģinat izvadīt nav definēts!" + "\n")
    o == o+1
    if kf == 1:
        for i in range(uzd):
            a = random.randrange(1, apj)
            b = random.randrange(1, apj)
            print(f"Kāds ir taisnustūra laukums ja tā malu garums ir šāds: {a} , {b}")
            f.write(f"Kāds ir taisnustūra laukums ja tā malu garums ir šāds: {a} , {b}" + "\n")
            atb = int(input("Laukums ir: "))
            f.write(str(atb) + "\n")
            if atb == a * b:
                print("Parezi!")
                f.write("Parezi!" + "\n")
                p+=1
            else:
                print("Neparezi!")
                f.write("Neparezi!" + "\n")
                n+=1
        print(f"No {uzd} piemēriem pareizi bija {p} uzdevumi un nepareizs {n}. Kopumā sekmīgi tika veikti {p*100/uzd}%") 
        f.write(f"No {uzd} piemēriem pareizi bija {p} uzdevumi un nepareizs {n}. Kopumā sekmīgi tika veikti {p*100/uzd}%" + "\n")           
    elif kf == 2:
        for i in range(uzd):
            c = random.randrange(1, apj)
            d = random.randrange(1, apj)
            print(f"Kāds ir laukums tristūrim ja tā malas garums ir {c} un augstums pret to malu ir {d}")
            f.write(f"Kāds ir laukums tristūrim ja tā malas garums ir {c} un augstums pret to malu ir {d}" + "\n")
            atb =int(input("Laukums ir: "))
            f.write(str(atb) + "\n")
            if atb == c*d/2:
               print("Parezi!")
               f.write
               p+=1
            else:
               print("Neparezi!")
               f.write
               n+=1
        print(f"No {uzd} piemēriem pareizi bija {p} uzdevumi un nepareizs {n}. Kopumā sekmīgi tika veikti {p*100/uzd}%")
        f.write
    elif kf == 3:
        for i in range(uzd):
            e = random.randrange(1, apj)
            print(f"Kāds ir apļa laukums, ja tā radius ir {e} pi vertību ņem kā 3.14")
            f.write
            atb =float(input("Laukums ir: "))
            f.write
            if atb == e*e*3.14:
                print("Parezi!")
                f.write
                p+=1
            else:
                print("Neparezi!")
                f.write
                n+=1
        print(f"No {uzd} piemēriem pareizi bija {p} uzdevumi un nepareizs {n}. Kopumā sekmīgi tika veikti {p*100/uzd}%")
        f.write
    elif kf == 4:
        for i in range(uzd):
            l = random.randrange(1, apj)
            k = random.randrange(1, apj)
            print(f"Kāds ir taisnustūra perimetrs ja tā malu garums ir šāds: {l} , {k}")
            f.write
            atb = int(input("perimetrs ir: "))
            f.write
            if atb == l+k*2:
                print("Parezi!")
                f.write
                p+=1
            else:
                print("Neparezi!")
                f.write
                n+=1
        print(f"No {uzd} piemēriem pareizi bija {p} uzdevumi un nepareizs {n}. Kopumā sekmīgi tika veikti {p*100/uzd}%")
        f.write        
    elif kf == 5:
        for i in range(uzd):
            a = random.randrange(1, apj)
            b = random.randrange(1, apj)
            c = random.randrange(1, apj)
            print(f"Kāds ir taisnustūra perimetrs ja tā malu garums ir šāds: {a} , {b} , {c}")
            f.write
            atb = int(input("Perimetrs ir: "))
            f.write
            if atb == a+b+c:
                print("Parezi!")
                f.write
                p+=1
            else:
                print("Neparezi!")
                f.write
                n+=1
        print(f"No {uzd} piemēriem pareizi bija {p} uzdevumi un nepareizs {n}. Kopumā sekmīgi tika veikti {p*100/uzd}%")
        f.write        
    elif kf == 6:
        for i in range(uzd):
            e = random.randrange(1, apj)
            print(f"Kāds ir apļa diamets, ja tā radius ir {e}")
            f.write
            atb =float(input("Diametra garums ir: "))
            f.write
            if atb == e+e:
                print("Parezi!")
                f.write
                p+=1
            else:
                print("Neparezi!")
                f.write
                n+=1
        print(f"No {uzd} piemēriem pareizi bija {p} uzdevumi un nepareizs {n}. Kopumā sekmīgi tika veikti {p*100/uzd}%")
        f.write        
    elif kf == 7:
        for i in range(uzd):
            e = random.randrange(1, apj)
            print(f"Kāds ir riņķa līnijas garums, ja tā radius ir {e} pi vertību ņem kā 3.14")
            f.write
            atb =float(input("Riņķa līnijas garums ir: "))
            f.write
            if atb == 2*3.14*e:
                print("Parezi!")
                f.write
                p+=1
            else:
                print("Neparezi!")
                f.write
                n+=1
        print(f"No {uzd} piemēriem pareizi bija {p} uzdevumi un nepareizs {n}. Kopumā sekmīgi tika veikti {p*100/uzd}%")
        f.write           
    elif kf == 8:
        for i in range(uzd):
            a = random.randrange(1, apj)
            b = random.randrange(1, apj)
            h = random.randrange(1, apj)
            print(f"Kāds ir trapeces laukums, ja tā pamatu garumi ir {a} , {b}  un augstums ir {h} ")
            f.write
            atb =float(input("Laukums ir: "))
            f.write
            if atb == a+b/2*h:
                print("Parezi!")
                f.write
                p+=1
            else:
                print("Neparezi!")
                f.write
                n+=1 
        print(f"No {uzd} piemēriem pareizi bija {p} uzdevumi un nepareizs {n}. Kopumā sekmīgi tika veikti {p*100/uzd}%")
        f.write                            
else:
    u = int(input("Vai vēlaties pildīt vēlreiz? Ja pildīsiet vēlrei ievadi-1: "))

    
    
print("Ja neizdodas aprēķināt kādu figūru var mēģināt aprēķinat ar šo  programu.")
import liana

x = int(input("Izvēlies vienu no figūrām, kuru aprēķināsi: riņķis-1 , trijstūris-2 , taisnstūris-3: "))
if x==1:
    y = int(input("Izvēlies, ko aprēķināsi;laukums-1, riņkā līnijas garums-2 , diametrs-3: "))
    if y==1:
        a = int(input("Ievadi rādiusu:"))
        print("Laukums ir", liana.rinka_lauk(a))
    elif y==2:
        b = int(input("Ievadi rādiusu:"))
        print("Perimetrs ir", liana.rinka_perimets(b))
    else:
        c = int(input("Ievadi rādiusu:"))
        print("Diametrs ir", liana.rinka_diamet(c))
elif x == 2:
    m = int(input("Izvēlies, ko aprēķināsi;laukums-1, perimetrs-2 :  "))
    if m==1:
        d = int(input("Ievadi trijstrūra augstumu(h): "))
        k = int(input("Ievadi trijstrūra malas garumu: "))
        print("Laukums ir", liana.trijs_laukums(d, k))
    else:
        a = int(input("Ievadi trijstrūra pirmo malu: "))
        b = int(input("Ievadi trijstrūra otro malu: ")) 
        c = int(input("Ievadi trijstrūra trešo malu: "))
        print("Perimetrs ir", liana.trijs_perimetrs(a, b, c))
else:
    g = int(input("Izvēlies, ko aprēķināsi;laukums-1, perimetrs-2, :  ")) 
    if g == 1:
        u = int(input("Ievadi taisnustūta īsāko malu: "))
        t = int(input("Ievadi taisnustūta garāko malu: "))
        print("Laukums ir", liana.cetrusturis_laukums(u, t))
    else: 
        u = int(input("Ievadi taisnustūta īsāko malu: "))
        t = int(input("Ievadi taisnustūta garāko malu: "))
        print("Perimetrs ir", liana.cetrusturis_perimetrs(u, t))

 #mos sito nevajadzēs

print( )
a = "Uzdevums- Izveidot sarakstu kurā ir noteikts skaits skailū un šo skaitu ievada cilvēks, programma aprēkina videjo aritmētisko, nosaka cik ir pāra un nepāra  skaiļu, cik ir pozitīvi un cik negatīvi skaiļi, skaiļus sakotnējā saraktā saliek pēc kartas augošā secībā jaunā sarakstā  " 

print(a)
print( )
sk = []
n = -1
while n < 20 or n > 50:
    n = int(input("Cik skaitļu būs saraksta? (Ievadiet skaitli intervālā no 20 līdz 50.)"))
    if n < 20:
        print("šis skaitlis neder,jo ir mazākas par 20. Ievadi vēlreiz:")
    elif n > 50:
        print("šis skaitlis neder, jo ir lielāks par 50. Ievadi vēlreiz:")
import random
summa = 0
for i in range(n):
    a = random.randrange(-100, 100)
    summa += a
    
    sk.append(a)
print(sk)
print("Visu skaitļu suma ir ", summa)
print()
o = int(input("Kāda ir vidējā aritmētiskā šajam saratam: "))
if o == summa/n:
    print("Tava atbilde ir pareiza malacis.")

m = min(sk)
l = max(sk)
print("Mazākā vertība sarakstā ir", m)
print("Lielākā vērtība sarakstā ir", l)
x=int(input("Ievadiet skaitli! kuru pievienosim izveidotajam sarakstas intervālā no -100 līdz 100:"))
sk.append(x)   

print("Jauniegūtais saraksts", sk)
sk.sort()
print("Izvadu sakartotu sarakstu augošā secībā", sk)

ne = []
pa = []
for num in sk:
    if num % 2 == 0:
        pa.append(num)
    else:
        ne.append(num,)    
print("Nepāra skaitļi ir šadi ", ne)
print()
print("Pāra skaitļi ir šadi ", pa)



    

