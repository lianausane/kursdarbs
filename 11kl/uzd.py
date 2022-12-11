
import random
import math
MAPE = "faili/"
fails = MAPE + "aprekini.txt"
f = open(fails, 'a', encoding="UTF-8")

failss = MAPE + "visskovaraprekinat.txt"
k = open(failss,'r', encoding="UTF-8" )


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
 
vārdnīca ={
    "Taisnstura laukuma aprēķināšanas formula" : "S=a*b",
    "Trijtūra laukuma aprēķināšanas formula" : "S=a*h/2",
    "Apļa laukuma aprēķināšanas formula" : "S=π*r*2",
    "Taisnstūra perimetra aprēķināšanas formula" : "P = 2*(a+b)",
    "Trijstūra perimeta aprēķināšanas formula" : "P = a+b+c",
    "Apļa diametra aprēķināšanas formula" : "d = 2*r",
    "Riņķa līnijas garuma aprēķināšanas formula" : "C=2*π*r",
    "Trapeces laukuma aprēķināšanas formula" : "S=((a+b)*h)/2",
}

print( )
print("Šis formulas varētu noderēt, pievērs uzmanību!")
for key, value in vārdnīca.items():
    print(f"{key} - {value}")

print( )

sk = [] 
for r in k:
    # rindas vērtība tiek pievienota sarakstam
    sk.append(r)
    # no faila nolasītā vērtība tiek izvadīta uz ekrāna
    print(r, end="")
    #print(type(r))



kf = int(input("Kuru figūras funkciju apreķināsim: "))
f.write("Kuru figūras funkciju apreķināsim: " + "\n")
uzd = int(input("Cik tādus uzdevumus pildisiet: "))
f.write("Cik tādus uzdevumus pildisiet: " + "\n")

f = True
while f:
    try:
        print(uzd)
        f = False    
    except: 
        
        print("Nepareizi levaddati")
        print ("piemeram: Drikst levadit tikai 1, 2, 3, 4, 5")
        

if kf == 1:
    for i in range(uzd):
        a = random.randrange(1, apj)
        b = random.randrange(1, apj)
        print(f"Kāds ir taisnustūra laukums ja tā malu garums ir šāds: {a} , {b}")
        f.write(f"Kāds ir taisnustūra laukums ja tā malu garums ir šāds: {a} , {b}" + "\n")
        atb = int(input("Laukums ir: "))
        f.write("Laukums ir: " + str(atb) + "\n")
        if atb == a * b:
            print("Pareizi!")
            f.write("Pareizi!" + "\n")
            p+=1
        else:
            print("Nepareizi!")
            f.write("Nepareizi!" + "\n")
            print("Paeizā atbilde ir",a * b )
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
            f.write("Laukums ir: " + str(atb) + "\n")
            if atb == c*d/2:
                print("Pareizi!")
                f.write("Pareizi!" + "\n")
                p+=1
            else:
                print("Nepareizi!")
                f.write("Nepareizi!" + "\n")
                print("Pareizā atbilde ir",c*d/2)
                n+=1
        print(f"No {uzd} piemēriem pareizi bija {p} uzdevumi un nepareizs {n}. Kopumā sekmīgi tika veikti {p*100/uzd}%")
        f.write(f"No {uzd} piemēriem pareizi bija {p} uzdevumi un nepareizs {n}. Kopumā sekmīgi tika veikti {p*100/uzd}%" + "\n")
elif kf == 3:
        for i in range(uzd):
            e = random.randrange(1, apj)
            print(f"Kāds ir apļa laukums, ja tā radius ir {e} pi vertību ņem kā 3.14")
            f.write(f"Kāds ir apļa laukums, ja tā radius ir {e} pi vertību ņem kā 3.14")
            atb =float(input("Laukums ir: "))
            f.write("Laukums ir:" + str(atb) + "\n")
            if atb == e*e*3.14:
                print("Pareizi!")
                f.write("Pareizi!" + "\n")
                p+=1
            else:
                print("Nepareizi!")
                f.write("Nepareizi!" + "\n")
                print("Paeizā atbilde ir",e*e*3.14 )
                n+=1
        print(f"No {uzd} piemēriem pareizi bija {p} uzdevumi un nepareizs {n}. Kopumā sekmīgi tika veikti {p*100/uzd}%")
        f.write(f"No {uzd} piemēriem pareizi bija {p} uzdevumi un nepareizs {n}. Kopumā sekmīgi tika veikti {p*100/uzd}%" + "\n")
elif kf == 4:
        for i in range(uzd):
            l = random.randrange(1, apj)
            k = random.randrange(1, apj)
            print(f"Kāds ir taisnustūra perimetrs ja tā malu garums ir šāds: {l} , {k}")
            f.write(f"Kāds ir taisnustūra perimetrs ja tā malu garums ir šāds: {l} , {k}" + "\n")
            atb = int(input("Perimetrs ir: "))
            f.write("Perimetrs ir: " + str(atb) + "\n")
            if atb == l+k*2:
                print("Parezi!")
                f.write("Parezi!" + "\n")
                p+=1
            else:
                print("Nepareizi!")
                f.write("Nepareizi!" + "\n")
                print("Paeizā atbilde ir",l+k*2 )
                n+=1
        print(f"No {uzd} piemēriem pareizi bija {p} uzdevumi un nepareizs {n}. Kopumā sekmīgi tika veikti {p*100/uzd}%")
        f.write(f"No {uzd} piemēriem pareizi bija {p} uzdevumi un nepareizs {n}. Kopumā sekmīgi tika veikti {p*100/uzd}%" + "\n")        
elif kf == 5:
        for i in range(uzd):
            a = random.randrange(1, apj)
            b = random.randrange(1, apj)
            c = random.randrange(1, apj)
            print(f"Kāds ir taisnustūra perimetrs ja tā malu garums ir šāds: {a} , {b} , {c}")
            f.write
            atb = int(input("Perimetrs ir: "))
            f.write("Perimetrs ir: " + str(atb) + "\n")
            if atb == a+b+c:
                print("Parezi!")
                f.write("Parezi!" + "\n")
                p+=1
            else:
                print("Nepareizi!")
                f.write("Nepareizi!" + "\n")
                print("Paeizā atbilde ir", a+b+c)
                n+=1
        print(f"No {uzd} piemēriem pareizi bija {p} uzdevumi un nepareizs {n}. Kopumā sekmīgi tika veikti {p*100/uzd}%")
        f.write(f"No {uzd} piemēriem pareizi bija {p} uzdevumi un nepareizs {n}. Kopumā sekmīgi tika veikti {p*100/uzd}%" + "\n")        
elif kf == 6:
        for i in range(uzd):
            e = random.randrange(1, apj)
            print(f"Kāds ir apļa diamets, ja tā radius ir {e}")
            f.write
            atb =float(input("Diametra garums ir: "))
            f.write("Diametra garums ir: " + str(atb) + "\n")
            if atb == e+e:
                print("Pareizi!")
                f.write("Pareizi!" + "\n")
                p+=1
            else:
                print("Nepareizi!")
                f.write("Nepareizi!" + "\n")
                print("Paeizā atbilde ir",e+e )
                n+=1
        print(f"No {uzd} piemēriem pareizi bija {p} uzdevumi un nepareizs {n}. Kopumā sekmīgi tika veikti {p*100/uzd}%")
        f.write(f"No {uzd} piemēriem pareizi bija {p} uzdevumi un nepareizs {n}. Kopumā sekmīgi tika veikti {p*100/uzd}%" + "\n")        
elif kf == 7:
        for i in range(uzd):
            e = random.randrange(1, apj)
            print(f"Kāds ir riņķa līnijas garums, ja tā radius ir {e} pi vertību ņem kā 3.14")
            f.write
            atb =float(input("Riņķa līnijas garums ir: "))
            f.write("Riņķa līnijas garums ir: " + str(atb) + "\n")
            if atb == 2*3.14*e:
                print("Pareizi!")
                f.write("Pareizi!" + "\n")
                p+=1
            else:
                print("Nepareizi!")
                f.write("Nepareizi!" + "\n")
                print("Paeizā atbilde ir", 2*3.14*e)
                n+=1
        print(f"No {uzd} piemēriem pareizi bija {p} uzdevumi un nepareizs {n}. Kopumā sekmīgi tika veikti {p*100/uzd}%")
        f.write(f"No {uzd} piemēriem pareizi bija {p} uzdevumi un nepareizs {n}. Kopumā sekmīgi tika veikti {p*100/uzd}%" + "\n")           
elif kf == 8:
        for i in range(uzd):
            a = random.randrange(1, apj)
            b = random.randrange(1, apj)
            h = random.randrange(1, apj)
            print(f"Kāds ir trapeces laukums, ja tā pamatu garumi ir {a} , {b}  un augstums ir {h} ")
            f.write
            atb =float(input("Laukums ir: "))
            f.write("Laukums ir:" + str(atb) + "\n")
            if atb == a+b/2*h:
                print("Pareizi!")
                f.write("Pareizi!" + "\n")
                p+=1
            else:
                print("Nepareizi!")
                f.write("Nepareizi!" + "\n")
                print("Paeizā atbilde ir",a+b/2*h )
                n+=1 
        print(f"No {uzd} piemēriem pareizi bija {p} uzdevumi un nepareizs {n}. Kopumā sekmīgi tika veikti {p*100/uzd}%")
        f.write(f"No {uzd} piemēriem pareizi bija {p} uzdevumi un nepareizs {n}. Kopumā sekmīgi tika veikti {p*100/uzd}%" + "\n")                            


    
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
elif x == 3:
    g = int(input("Izvēlies, ko aprēķināsi;laukums-1, perimetrs-2, :  ")) 
    if g == 1:
        u = int(input("Ievadi taisnustūta īsāko malu: "))
        t = int(input("Ievadi taisnustūta garāko malu: "))
        print("Laukums ir", liana.cetrusturis_laukums(u, t))
    else: 
        u = int(input("Ievadi taisnustūta īsāko malu: "))
        t = int(input("Ievadi taisnustūta garāko malu: "))
        print("Perimetrs ir", liana.cetrusturis_perimetrs(u, t))
else:
    print("Mainīgais kuru mēģinat izvadīt nav definēts!")        

print("Papildus veidota datu struktūra tuple")
tuple = ("tristūris", "taisnstūris", "aplis", )
print(tuple)
 



    

