# Setup
- copy hw2.py as hw3.py
- pip install CProfileV
- create profile output files: python -m cProfile -o output_file hw3.py --n 999
- print profile output: python printprofile.py

# Analyse
- for n very large: isperfect() function takes way less time if square root is perfect and, obviously lowerupper() takes no time and mysqrt() as well not much
- for n is large and not perfect (e.g. n= 999999):  isperfect() has many calls (2286) but getLowUpper() takes a lot of time per call (7.218) as well as mysqrt() (6.878)
- results in output files, print with script printprofile.py

# Time Complexity
### isperfect()
- bestcase O(1): for n=0 and n=1
- worst case O(n): square root is not perfect so the loop runs n times
### getLowUpper()
- best case O(1): perfect square root, first iteration in first while loop and skipping of second while loop
- worst case O(n): not a perfect square root, both while loops are iterating n times
### mysqrt():
- best case O(1): for n=0 and n=1
- worst case O(n): first if case O(1), isperfect() is O(n), getLowUpper() is O(n), while-loop is O(nlog(n))
- so mysqrt() has a O(nlog(n)), depending on isperfect() and getLowUpper() functions


# Optimization

e.g. n=999999
### isperfect()
- while loop instead of for loop that just iterates max. till sqrt(n): instead of 144.617s now: 0.433s (O(sqrt(n)))
- vectorization: broadcasting with numpy leads to O(0.1*n), simply O(n), and better runtime (2.215s)

### getLowUpper()
- vectorization: broadcasting with numpy leads to O(n) and runtime of 0.303s

### mysqrt()
- without taking helper functions (for n=999999: 0.193s) and O(1)
- vectorization in while loop does neither improve runtime nor time complexity
- overall optimization: runtime from 174.309s to 0.202s improved; time complexity O(nlogn) because of binary search 

# Documents
- edited python file: hw3.py
- output files with n=999999 (large and not perfect square root): output_original, output_optimized
- for printing profile outputs: printprofiles.py  