def selection_sort(liste):
    for i in range(0,1):
        for j in range(len(liste)-i-1):
            if liste[j] > liste[j+1]:
                tempo = list[j]
                liste[j] = list[j+1] 
                liste[j+1] = tempo
    return liste
liste = [2, 5, 17, 13, 25, 55, 78, 98]
print(selection_sort(liste))
