# k-Means Algorithmus 

complexity: 
O(N*I*k) N = datapoints, I = iterations, k = number of cluster

It only works for non numpy generated data 
and only 2 dimensional data 


Ausgangssituation 
- Objekte besitzen Distanzfunktion 
- für jedes Cluster kann ein Clusterzentrum bestimmt werden ("Mittelwert")
- Anzahl k der Cluster wird vorgegeben - ich wähle 3 aufgrund der Folien 

Basis-Algorithmus 
1. (Initialisierung): K Clusterzentren werden zufällig gewählt
2. (Zuordnung): Jedes Objekt wird dem nächstgelegenen Clusterzentrum zugeordnet 
3. (Clusterzentren): Für jedes Cluster wird Clusterzentrum neu berechnet 
4. (Wiederholung): Abbruch, wenn Zuordnung unverändert, sonst zu 2.






