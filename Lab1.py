# Nathaniel_Copeland
# CSCI_3300
# 8_25_2019
# Dr.K
# HW1
import itertools

def combination(k):
    return (''.join(p) for p in itertools.product('ATCG', repeat=k))#returns all combinations of length k with ther letters ATCG

def hamming_distance(pattern, seq):#gets the hamming distance and returns it to motif
    return sum(c1 != c2 for c1, c2 in zip(pattern, seq))

def getKmers(s, k):
    for i in range(1 + len(s) - k):
        yield s[i:i+k] #adds all the kmers from the same DNA strand to the same list
    #print(s)
def matchFinder(k, d, DNA):
    pattern = set()
    for combo in combination(k): #gets combinations
        if all(any(hamming_distance(combo, pat) <= d #best case found on stackoverflow, if all the hamming distancs between the kmers compared, then the kmer is added to the final set()
                for pat in getKmers(string, k)) for string in DNA):#best case found on stackoverflow and is saying for each kmer returned for each DNA strand
            pattern.add(combo)
    return pattern #returns the set created on the final kmers that made it through

samples = open('lab1.txt', 'r')
input=[]
for line in samples:
	input.append(line.strip())

print('In the the DNA strand samples of ', input)
print('The Motifs of the list are ', matchFinder(4, 1, input))