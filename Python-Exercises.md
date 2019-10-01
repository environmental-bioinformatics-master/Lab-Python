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

## 2. Frequent kmer problem
We use the term k-mer to indicate a string of DNA of length *k*. You can think of them loosely as words within a DNA sequence. For example:
> 'ATCG' is a 4-mer (k-mer of length 4)
> 'ATTGGGCT' is a 8-mer (kmer of length 8)

**How many 2-mers are there? How many 8-mers? What is the general formula for calculating the number of possible kmers?**

k-mers of various lengths are used across biology to facilitate the analysis of sequence information. For example, k-mers are used for:
1. The assembly of genomes and transcriptomes through the construction of De Bruijn graphs (more on this later)
2. Identify protein coding regions
3. Identify species within metagenomes 
4. Detection of repeats and transposable elements
5. Evidence of recombination
6. Identifying contamination or misassembly

And many more! We will talk about k-mers more in future but for today-- let's just think about how to count them. 

Let's write a function that for a given pattern counts the number of times that pattern occurs within a string. This type of thing already exists within the `re` package-- feel free to look that up later. But for now, let's try doing this our selves:

First, let's write a function called `PatternCount` that counts the number of times a pattern occurs in a string. The idea being that you can start with some sequence and search for  a particular k-mer (pattern). 

Let's work with this pseudocode and convert it into python. (Note: `|` indicates the length of the item and `<-` indicates assignment) 
```
PatternCount(Text, Pattern)
	count <- 0
	for i<- 0 to |text| - |Pattern|
		if Text(i, |Pattern|) = Pattern
			count <- count + 1
	return count
```

Alright, now we lets make a function called `PatternFinder`. Provided with a sequence (string) and a k-mer length (integer) the program should move through and identify all the possible k-mers in that sequence and save them to an array called Kmers. 

``` 
PatternFinder(Text, k)
	L <- |Text|
	Kmers <- empty array
	for n<- 0 to L - k 
		Kmers <- Text[n, k]
	return Kmers
```

> What kind of data type should we use to store our k-mers? 

Now let's think about how we could combine these two functions to create a new function called `FrequentWords`. `FrequentWords` should take a Sequence and a word length (k) and calculate how many times each of the k-mers occurs in  sequence and then returns the most frequently occurring k-mer.

