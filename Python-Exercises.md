# Python Exercises
@(Teaching)

## 1. Triplet codon translation problem

We are all familiar with the paradigm in biology:
 > **DNA &rarr; RNA  &rarr; Protein**

Translation is the process by which ribosomes synthesize proteins from transcribed RNA. In translation mRNA is decoded to produce a specific amino acid chain which is ultimately folded and turned into an active protein. The ribosome decodes by facilitating the binding of complementary tRNA anticodons to mRNA codons. The tRNA carry specific amino acids that are chained together. Thus, each amino acid is matched to a three nucleotide subsequence of mRNA. 

### Translating DNA (RNA) sequences to amino acids 
The first thing we have to do is read in the protein:codon translation dictionary. Let's take a look at that file (`data/std-code.tab`). 
```
AAA K Lys
AAC N Asn
AAG K Lys
AAT N Asn
```

Let's write some code to read this data into python in a usable format. What data type should we use? 

Now, we are going to write a python script called `get_protein()` that takes an input sequence and returns a protein sequence. Let's figure out the pseudo-code of what we want this function to do? 

Things to consider: 
1. What if our sequence isn't mod(3) -- will our function still work? 
2. How can we ensure that the user only inputs ATCG? 
