# Spectral
# Language: Python
# Input: CSV (network)
# Output: prefix (for eigenvalues and eigenvectors)
# Tested with: PluMA 1.0, Python 3.6

PluMA plugin to compute eigenvectors for spectral clustering (Meila and Shi, 2001).  
This plugin accepts as input a network in CSV format, with both rows and columns representing
nodes and entry (i, j) the weight of the edge from node i to node j.

The plugin then computes a sorted list of eigenvalues and eigenvectors of the Laplacian matrix (defined by D-A where
D is a diagonal matrix where the elements are column sums of the adjacency matrix defined in 
the input CSV file.  These will be output into two files: prefix.eigenvalues.txt and prefix.eigenvectors.csv.
The format of the eigenvalues file consists of lines of the format:

node,eigenvalue

Eigenvalues in the file should be sorted from smallest to largest.  These in turn can be used
to partition clusters in various ways (which is why we left that part open).

The eigenvectors in the other output file will be of the format:

node,eigenvector

Nodes will be placed in the same order as the eigenvalue output file; hence each eigenvector
corresponds to the eigenvalue on the same line in the eigenvalue output file. 
