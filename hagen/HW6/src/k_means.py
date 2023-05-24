
'''
This is the sixth homework, where we try to implement k-means.
'''

import numpy as np
import matplotlib as plt


def distance(x, y) :
    """
     Function takes two coordinates (both tuples) and calculates their Euclidean distance.
    """
    return np.sqrt( (x[0] - y[0])**2 + (x[1] - y[1])**2 )


def average(points):
    """
     Function calculates average values (returned as tuple) for a list of coordinate points.
    """
    #sum_x  = 0
    #for point in points:
     #    sum_x += 
    x = np.average(np.array(points)[:,0])
    y = np.average(np.array(points)[:,1])
    
    return (x,y)


def k_means(k, data):
    """
     Function for k-means algorithm: 
     - returns a list of centroids and their subsets in the form of a list of the centroids + subsets, where subset is also a list.
     - for a given dataset (list) and a number of clusters k (int)
    """
     # choose initial centroids:
    initial_centroids = []
    for i in range(k):
        initial_centroids.append(data.copy()[i])


     # initiate subsets: first entry is id of centroid (0 to k-1), second entry is the subset of points as a list (now empty).
     # The position of the subset is later used as an ID.
    subsets = []
    for centroid in initial_centroids:
        subset = []
        subsets.append( [centroid, subset] )   


     # New list for assortment, which has the order of points in "data". All points are assorted to the first cluster 0 by default:
    assortment = [0] * len(data)

    for point in data:
        subsets[0][1].append(point)


     # Loop over all points in data and assort them to the centroid with minimal distance.
     # Do this until no changes occurr in assortment.
    flag = True
    
    while flag:
        flag = False  #If no change is made, while-loop will not be executed another time  
        point_index = 0
    
        for point in data:
        
            for s in subsets:
                old_distance = distance(point, subsets[assortment[point_index]][0]) #calculate distance to old centroid
                this_distance = distance(point, s[0]) #calculate distance to this centroid
            
                if this_distance < old_distance:
                    subsets[assortment[point_index]][1].remove(point)   #remove point from old subset
                    assortment[point_index] = subsets.index(s)   #Set assortment of point to new centroid id
                    subsets[assortment[point_index]][1].append(point)  #append point to new subset
                    flag = True   #If a point switches cluster, while-loop is executed again.
        
            point_index+=1
        
        # Recalculate centroids for all subsets:
        for s in subsets:
            s[0] = average(s[1])


    # return statement:
    return subsets                      



def main () :

    # Try algorithm for test data:
    small_data = [ (1,2), (3,4), (4,5), (6,3), (2,3), (8,2), (3.4, 2.3), (8,9), (2,2), (0,-1), (-3,-1) ]

    my_subsets = k_means(3, small_data)
    #print(my_subsets)
    
    # Try algorithm for gaussian data from lecture:
    rng = np.random.default_rng(seed = 1234)
    cl1 = rng.multivariate_normal([-2,-2], [[1,-0.5],[-0.5,1]], size=100)
    cl2 = rng.multivariate_normal([1,0], [[1,0],[0,1]], size=150)
    cl3 = rng.multivariate_normal([3,2], [[1,-0.7],[-0.7,1]], size=200)
    pts = np.concatenate((cl1,cl2,cl3))
    

    # Cast data into type list of lists
    pts = list(pts)
    for i in range(len(pts)):
        pts[i]= list(pts[i])
    #print(pts[:10])


    # Clustering for k = 3
    gaussian_dist = k_means(3, pts)
    print("These are the 3 centroids:")
    i = 0
    for subset in gaussian_dist:
        print(f"Cluster Number {i+1}: {gaussian_dist[i][0]}")
        i+=1

             
    # You could try different k up to 10:
    #for k in range(2, min(11, len(pts))): # making sure that k <= n
    #    results = k_means(k, pts) 
    #    print(f"\n\nResults for {k} clusters:") 
    #    i=0 
    #    for subset in results:
    #        print(f"\nCluster Number {i+1}: {results[i][0]}")
    #        i+=1      
              
 


if __name__ =="__main__" :
        main()
