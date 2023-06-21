
# Planning 

## Initialise: 
 - initialise the algorithm with K centers, picked randomly. 
 - use array indexing with the numpy function np.random.choice(a, size=None, replace=True, p=None) to select K random points from the given dataset. 
 - name the center array "centers" 


 
## Assignment step (runs through a loop of assigned iterations): 
 - for each centre in centers (loop over K):
         
         * calculate the distance (np.linalg.norm) of each point to the current center
         * append the distance to an array -> with each column representing the norms for a specific center. -> name the array "normed" 
 - now use numpy argmin across each column of the matrix (axis = 1) to set the label of the cluster for each point. 
 
## Update step (also runs through loop of assigned iterations): 
 - for each column in "normed" matrix (loop): 
     - update each centre to be the new centre
    