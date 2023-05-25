<h1>Homework 6</h1>
<h4>--Paula Hagen--</h4>  
   
   
<h2>Approach</h2>
1. Write Function distance(), which calculates Euclidean Distance of two points in coordinate system.  
2. Write function average(), which calculates the average coordinates of a list of (x,y) points.   
In Function k_means():  
3. Choose first k points in data set as centroids (copy values). It has been shown, that the choice of the centroids is not very relevant for the result, so we do not have to choose them randomly.   
4. Loop over points and put them each to the closest centroid => smallest distance(). Each centroid and its subset are stored in a list. The assortment of the points is also stored in a separate list.
5. Recalculate all centroids as averages of their subsets.
6. Do steps 4-5 until lists stay the same.  
7. (Do steps 3-6 for each k).   
8. Try algorithm for gaussian data from lecture.  

   
  
<h2>Efficiency</h2>
   
I used  
`time python k_means.py`  
to check the overall time used by the programme using the gaussian data from the lecture. The total time was 0.233 for k = 3 and 1.185 for repeating the process for all k up to 10 (2<=k<=10).   
Using a bigger data set will probably lead to a high execution time, as the time complexity of the code is minimum k^2*n (depending on while-loop iterations). Right now, the while-loop iterates until there are no further changes in assortement. For a bigger data set, I would change this into a set number of iterations, e.g., or until a certain percent of the clusters doesn't change anymore. 