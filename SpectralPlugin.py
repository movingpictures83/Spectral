import numpy
import random
import spectral
import math

class SpectralPlugin:
   def input(self, filename):
      filestuff = open(filename)#+".csv", 'r')
      self.firstline = filestuff.readline()
      self.bacteria = self.firstline.split(',')
      self.bacteria.remove('\"\"')
      self.n = len(self.bacteria)

      #self.A = numpy.matrix(numpy.zeros([self.n, self.n]))
      self.A = numpy.zeros([self.n, self.n])
 
      i = 0
      for line in filestuff:
         self.bacteria[i] = self.bacteria[i].strip()
         self.bacteria[i] = self.bacteria[i][1:len(self.bacteria[i])-1] # Remove quotes
         contents = line.split(',')
         for j in range(self.n):
              if (i != j):
                 #self.A[i,j] = float(contents[j+1])
                 self.A[i][j] = float(contents[j+1])
              else:
                 self.A[i][j] = 0.0
         i += 1

      #pathwayfile = open(filename+".pathways.txt", 'r')
      #self.K = -1  # The first line should not count
      #for line in pathwayfile:
      #   self.K += 1

   def run(self):
      L = spectral.getSignedLaplacian(self.A)

      #print type(L)
      #print dir(L)
      #print (L.transpose() == L).all()
      for i in range(self.n):
         for j in range(i+1, self.n):
            #L[i, j] = numpy.float32(L[i, j])
            L[i, j] = int(round(L[i, j], 12)*(10**12))
            L[j, i] = L[i, j]
            #if (abs(L[i, j]) > 1):
            #print L[i, j], i, j
            #raw_input()
            #print L[80, i], L[i, 80], numpy.float32(L[80, i])
      print "EIGENVALUES:"
      #import sympy
      #M = sympy.Matrix(L.tolist())
      #M.eigenvals()
      
      print numpy.linalg.eig(L[0:80, 0:80])[0]
      #print L.round(12)*(10**12)
      #print numpy.linalg.eig(L.round(12)*(10**12))[0]
      #raw_input()
      self.eigenVectors = spectral.getSortedEigenVectors(L)
      #print self.eigenVectors
      #raw_input()

   def output(self, filename):
      #print spectral.spectralClustering(self.A, self.K)
      #return
      filestuff2 = open(filename, 'w')
      filestuff2.write(self.firstline)   # CSV
      #filestuff2.write("name\tspectralWeight\n")
      for i in range(self.n):
         filestuff2.write(self.bacteria[i]+',')
         for j in range(self.n):
            #filestuff2.write(self.bacteria[i]+' (pp) '+self.bacteria[j]+'\t'+str(float(self.eigenVectors[i, j]))+'\n')
            filestuff2.write(str(float(self.eigenVectors[i, j])))
            if (j < self.n-1):
               filestuff2.write(",")
            else:
               filestuff2.write("\n")

