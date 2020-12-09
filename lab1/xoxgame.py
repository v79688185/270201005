tableliste = [[1,2,3],[4,5,6],[7,8,9]]
sıra = 1
kazanan = True
for i in tableliste:
    print(f"{i[0]}|{i[1]}|{i[2]}") 
while kazanan:
    if  sıra % 2 == 1:
        xharfi = int(input("sıra xte x harfini gireceğiniz sayıyı seçin: "))
        for i in tableliste:
            if xharfi in i:
                i[i.index(xharfi)] = "x"
    elif sıra % 2 == 0:
        yharfi = int(input("sıra o da o harfini gireceğiniz sayıyı seçin: "))
        for i in tableliste:
            if yharfi in i:
                i[i.index(yharfi)] = "o"
    for i in tableliste:
        print(f"{i[0]}|{i[1]}|{i[2]}")        
    sıra = sıra + 1 
    for i in tableliste :
        if i[0] == i[1] == i[2] == "x":
            print("x kazandı")
            kazanan = False
            break
        elif i[0] == i[1] == i[2] == "o":
            print("o kazandı")
            kazanan = False
            break
    if tableliste[0][0] == tableliste[1][1] == tableliste[2][2] == "x" or tableliste[0][2] == tableliste[1][1] == tableliste[2][0] == "x": 
        print("x kazandı")
        kazanan = False
    elif tableliste[0][0] == tableliste[1][1] == tableliste[2][2] == "o" or tableliste[0][2] == tableliste[1][1] == tableliste[2][0] == "o":      
        print("o kazandı")
        kazanan = False 
    elif tableliste[0][0] == tableliste[1][0] == tableliste[2][0] == "x" or tableliste[0][1] == tableliste[1][1]==tableliste[2][1] == "x" or tableliste[0][2]== tableliste[1][2]==tableliste[2][2] == "x":
        print("x kazandı")
        kazanan = False
    elif tableliste[0][0] == tableliste[1][0] == tableliste[2][0] == "o" or tableliste[0][1] == tableliste[1][1]==tableliste[2][1] == "o" or tableliste[0][2]== tableliste[1][2]==tableliste[2][2] == "o":     
        print("o kazandı")
        kazanan = False 
    