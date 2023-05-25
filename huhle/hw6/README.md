# Complexity of the k-means algorithm
The highest complexity comes from the outer and the inner
loop of the k-means algorithm. The outer loop iterates
'iterations' times while the first inner loop iterates
len(pts) times (which is more iterations than in the second
inner loop: k = 3). Finding the minimum distance with
np.argmin has a complexity of O(k). Overall the complexity
of the k-means algorithm is O(iterations * len(pts) * k).