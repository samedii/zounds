import numpy as np
from scipy.cluster.vq import kmeans
from scipy.spatial.distance import cdist
from learn.learn import Learn


# KLUDGE: I've added indim and hdim so this class can be used 
        # as a NeuralNetwork-derived class
class KMeans(Learn):
    
    def __init__(self,n_centroids):
        Learn.__init__(self)
        self.n_centroids = n_centroids
        self.codebook = None
        
        
    
    @property
    def indim(self):
        return self.codebook.shape[1]
    
    @property
    def hdim(self):
        return self.codebook.shape[0]
    
    def train(self,data,stopping_condition):
        self._indim = data.shape[1]
        codebook,distortion = kmeans(data,self.n_centroids)
        self._hdim = len(codebook)
        self.codebook = codebook
    
    def __call__(self,data):
        dist = cdist(np.array([data]),self.codebook)[0]
        best = np.argmin(dist)
        feature = np.zeros(len(self.codebook),dtype = np.uint8)
        feature[best] = 1
        return feature