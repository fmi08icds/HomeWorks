# Homework 6
## Implement your version of k-means and comment on the complexity.

### Files
- *hw6tests.ipynb*: shows some of my approach and testing
- *hw6.py*: Final simple and intuitive implementation of k-means (good way to see the complexity)

### Complexity
- most obvious is the complexity of the nested loop which contains $p$ points times $k$ centroids so $O(k\cdot p)$.
- now taking into account the loop executing the calculation `max_iter` times (or less if centroid is already in perfect position). Lets say the computation executes $i$ times. This would conclude to $O(k\cdot p\cdot i)$.
- Another point to consider is the dimension $d$ of the given points, which in this case is always 2. This would conclude the final complexity to $O(k\cdot p\cdot i\cdot d)$.