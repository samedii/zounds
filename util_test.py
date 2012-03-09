import numpy as np
import unittest
from util import pad


class PadTests(unittest.TestCase):
    
    def test_pad_onedim_desired(self):
        a = np.array([1,2,3])
        b = pad(a,3)
        self.assertEqual(a.shape,b.shape)
        self.assertTrue(np.allclose(a,b))
        
    def test_pad_onedim_longer(self):
        a = np.array([1,2,3,4])
        b = pad(a,3)
        self.assertEqual(a.shape,b.shape)
        self.assertTrue(np.allclose(a,b))
        
    def test_pad_onedim_shorter(self):
        a = np.array([1,2,3])
        b = pad(a,4)
        self.assertEqual(4,len(b))
        self.assertEqual(0,b[-1])
        
    def test_pad_twodim_desired(self):
        a = np.random.random_sample((10,10))
        b = pad(a,10)
        self.assertEqual(a.shape,b.shape)
        self.assertTrue(np.allclose(a,b))
    
    def test_pad_twodim_longer(self):
        a = np.random.random_sample((12,10))
        b = pad(a,10)
        self.assertEqual(a.shape,b.shape)
        self.assertTrue(np.allclose(a,b))
        
    def test_pad_twodim_shorter(self):
        a = np.random.random_sample((10,10))
        b = pad(a,13)
        self.assertEqual(13,b.shape[0])
        self.assertTrue(np.allclose(a,b[:10]))
        self.assertTrue(np.all(b[10:] == 0))
        
    def test_pad_list(self):
        l = [1,2,3]
        b = pad(l,4)
        self.assertEqual(4,len(b))
        self.assertEqual(0,b[-1])

from util import recurse,sort_by_lineage
class Node:
    
    def __init__(self,parents=None):
        if not parents:
            self.parents = []
        else:
            self.parents = parents
    
    @recurse
    def ancestors(self):
        return self.parents
    
class RecurseTests(unittest.TestCase):
    
    def test_root(self):
        n = Node()
        self.assertEqual(0,len(n.ancestors()))
        
    def test_single_parent(self):
        root = Node()
        child = Node(parents=[root])
        a = child.ancestors()
        self.assertEqual(1,len(a))
        self.assertTrue(root in a)
        
    def test_multi_ancestor(self):
        root = Node()
        c1 = Node(parents=[root])
        c2 = Node(parents=[root])
        gc1 = Node(parents=[c1,c2])
        a = gc1.ancestors()
        self.assertEqual(3,len(a))
        self.assertTrue(root in a)
        self.assertTrue(c1 in a)
        self.assertTrue(c2 in a)

class SortByLineageTests(unittest.TestCase):
    
    def test_single_parent(self):
        self.fail()
        
    def test_multi_ancestor(self):
        self.fail()
        
        