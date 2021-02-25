Written by: Haruki Yoshida, Jake Martens, Martin Bernard, Kristin Albright

Python program that takes a text file of an RNA sequence and outputs a matrix, paired RNA sequence, and bracket notation. The program implements the Nussinov algorithm in order to do this. 

preconditions: each RNA sequence must be on its own line in the input file ("sequence.txt"). Each nucleotide must be followed by a space. For example "A U G C G" is acceptable, by "AUGCG" is not. To change the data, simply change file "sequence.txt". To run, type "python3 Nussinov.py" in terminal.

Output details:
We visualized the matrix so we can see the solved matrix. We filled the lower half with zeros to make the visualization clear but these should be empty in the real world. Also, we have a bracket notation of the pairings. We print out so we have the origianl RNA string and the bracket notations below it.