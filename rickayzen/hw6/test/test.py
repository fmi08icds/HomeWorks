import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname('__file__'),".."))
from kmeans import eucl_norm, k_means_iteration
from numpy.linalg import norm
import numpy.testing as npt

class TestKMeans(unittest.TestCase):
        
    def test_eucl_norm(self):
        print("testing euclidean norm")
        v = [0]
        self.assertEqual(eucl_norm(v),norm(v))
        v = [-1]
        self.assertEqual(eucl_norm(v),norm(v))
        v = [10]
        self.assertEqual(eucl_norm(v),norm(v))
        v = [-1,1]
        self.assertEqual(eucl_norm(v),norm(v))
        v = [-5,0,10]
        self.assertEqual(eucl_norm(v),norm(v))
        v = [0,1,2.65,3,4]
        self.assertEqual(eucl_norm(v),norm(v))
        v = [5/3,-1.5,4.5,-2.5]
        self.assertEqual(eucl_norm(v),norm(v))


    def test_k_means_iteration_1d(self):
        print("testing k_means_iteration for 1 dimensional vectors")
        v = [10,0]
        k=[0]
        cluster, new_k = k_means_iteration(v,k)
        npt.assert_array_equal(cluster,[[10,0]])
        npt.assert_array_equal(new_k,[5])
        v = [0,3,6,9,12]
        k = [3,8]
        cluster, new_k = k_means_iteration(v,k)
        npt.assert_array_equal(cluster,[[0,3],[6,9,12]])
        npt.assert_array_equal(new_k,[1.5,9])
        

    def test_k_means_iteration_2d(self):
        print("testing k_means_iteration for 2 dimensional vectors")
        v = [[0,0],[1,4],[-1,-2],[4,3]]
        k = [[0,0],[4,3]]
        cluster, new_k = k_means_iteration(v,k)
        npt.assert_array_equal(cluster,[[[0,0],[-1,-2]],[[1,4],[4,3]]])
        npt.assert_array_equal(new_k,[[-.5,-1],[2.5,3.5]])


    def igtest_k_means_iteration_3d(self):
        print("testing k_means_iteration for 3 dimensional vectors")
        v = [[0,0,0],[2,1,4],[-1,-1,-2],[1,4,3],[3,5,-7],[-1,2,-3]]
        k = [[0,0,0],[2,1,4]]
        cluster, new_k = k_means_iteration(v,k)
        npt.assert_array_equal(cluster,[[[0,0,0],[-1,-1,-2],[3,5,-7],[-1,2,-3]],[[2,1,4],[1,4,3]]])
        npt.assert_array_equal(new_k,[[.25,1.5,-3],[1.5,2.5,3.5]])


if __name__ == '__main__':
    unittest.main()
