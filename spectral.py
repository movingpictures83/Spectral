import math
from numpy import linalg as LA
import numpy as np
def KmeansClust(data, K, iterations = 100):
         
    if isinstance(data, dict) == False:
        raise TypeError('points data-set must be a dictionary')
     
    dim = -1
    for key in data :
        if dim == -1 :
            dim = len (data[key])
        elif len (data[key]) != dim:
            raise ValueError('Data set contains points with different dimensions')
                 
    centers = []  # contains K np.array() points
    clusters = [] # contains K array of keys
     
    ## initialize K centers
    ## TODO Randomized
    for key in data :
        centers.append(data[key])
        if len(centers) >= K :
            break
     
    while iterations >= 0 :
        ## K clusters
        clusters = [ [] for i in range(0,K) ]
         
        ## Assign points 
        for key in data :
            p = data[key]
            idx = 0
            min_dist = 100000000
             
            ## find the closest center to point p
            for i in range(0, K) :
             
                d2 = dist(p, centers[i])
             
                if d2 < min_dist :
                    idx = i
                    min_dist = d2
     
            clusters[idx].append(key)
         
        ## Calculate new centers
        for i in range(0,K) :
            centers[i] = np.zeros(dim)
            clust_sz = len(clusters[i])
            for key in clusters[i] :
                np.add(centers[i], p, out=centers[i], casting="unsafe")  # For newer numpy
                
            centers[i] = centers[i] / clust_sz
        iterations -= 1
             
    return clusters

'''
adjacency matrix
'''
def spectralClustering(A, K):
     
    if not isinstance(A, np.matrix) :
        A = np.matrix(A)
    
    if A.shape[0] != A.shape[1] :
        raise Exception('A must be a square matrix')

    if A.shape[0] != A.shape[1] :
        raise Exception('A must be a square matrix')
    
    if K > len(A) :
        raise Exception('K must be <= size of A')
    
    L = getSignedLaplacian(A)

    n = len(A)
        
    mat = getSortedEigenVectors(L)
    
    data = {}
    for nod in range(0,n) :
        data[nod] = np.squeeze(np.asarray(mat[nod,:K]))
     
    return KmeansClust(data,K)


def getSortedEigenValuesAndVectors(L, bac):
#def getSortedEigenVectors(L):
    n = len(L)
    e = LA.eig(L)
    E = []
    V = []
    C = []
    B = []
    for i in range(0,n) :
        eigenvalue = e[0][i]
        eigenvector = np.squeeze(np.asarray(e[1][:,i]))
        C.append([bac[i], eigenvalue , eigenvector]) 
    C = sorted(C, key=lambda tup: tup[1])
    
    for i in range(0, n) :
        V.append(C[i][2].tolist())
        E.append(C[i][1]) 
        B.append(C[i][0])   

    #V = np.matrix(V).transpose()
    return B, E, V


def getSignedLaplacian(A):
    D = np.zeros([len(A), len(A)])
    for i in range(len(A)):
       for j in range(len(A)):
          if (i == j):
             D[i][j] = sum(A[i])
          else:
             D[i][j] = -A[i][j]
    return D

def dist(p1, p2):
    return math.sqrt(sum((p1 - p2) ** 2))


if __name__ == "__main__" :
    def addEdge( A, u,v,w):
        A[u,v] = w
        A[v,u] = w
    A = np.zeros((6,6))
    addEdge(A,0,1,1)
    addEdge(A,0,2,1)
    addEdge(A,1,2,1)
    addEdge(A,2,3,-1)
    
    addEdge(A,3,4,1)
    addEdge(A,4,5,1)
    addEdge(A,4,5,1)
    
    clust = spectralClustering(A, 2)
