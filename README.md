# RecupElements2list
Récupérer des éléments communs à deux listes 
Dans cet exercice, nous passons par les sets pour récupérer les éléments communs à deux liste.

Pour convertir une liste en set, rien de plus facile, on utilise la fonction set :

sliste_01 = set(liste_01) 

Une fois que nos deux listes sont converties en set, nous pouvons utiliser des méthodes pour récupérer l'intersection, la différence et plein d'autres opérations du même style :

intersect = sliste_01.intersection(sliste_02) 

Il ne nous reste plus qu'à re-convertir notre set résultant en liste avec la fonction list :

resultat = list(intersect) 
