liste_01 = [1, 5, 6, 7, 9, 10, 11]
liste_02 = [2, 3, 5, 7, 8, 10, 12]
     
sliste_01 = set(liste_01)
sliste_02 = set(liste_02)
     
intersect = sliste_01.intersection(sliste_02)
print(list(intersect))