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

      self.A = numpy.zeros([self.n, self.n])
 
      i = 0
      for line in filestuff:
         self.bacteria[i] = self.bacteria[i].strip()
         self.bacteria[i] = self.bacteria[i][1:len(self.bacteria[i])-1] # Remove quotes
         contents = line.split(',')
         for j in range(self.n):
              if (i != j):
                 self.A[i][j] = float(contents[j+1])
              else:
                 self.A[i][j] = 0.0
         i += 1


   def run(self):
      L = spectral.getSignedLaplacian(self.A)

      for i in range(self.n):
         for j in range(i+1, self.n):
            L[i, j] = int(round(L[i, j], 12)*(10**12))
            L[j, i] = L[i, j]

      self.sortedBacteria, self.eigenValues, self.eigenVectors = spectral.getSortedEigenValuesAndVectors(L, self.bacteria)

   def output(self, filename):
      filestuff1 = open(filename+".eigenvalues.csv", 'w')
      filestuff2 = open(filename+".eigenvectors.csv", 'w')
      for i in range(self.n):
         filestuff1.write(self.sortedBacteria[i]+',')
         filestuff1.write(str(self.eigenValues[i])+"\n")
         filestuff2.write(self.sortedBacteria[i]+',')
         for j in range(self.n):
            filestuff2.write(str(self.eigenVectors[i][j]))
            if (j < self.n-1):
               filestuff2.write(",")
            else:
               filestuff2.write("\n")

