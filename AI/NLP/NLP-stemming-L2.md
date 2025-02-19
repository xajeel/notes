# 2. Stemming

Stemming is a technique used in natural language processing to reduce inflected (or sometimes derived) words to their word stem, base or root form. 

It is often used in various applications like text mining, information retrieval (Google uses stemming for its search engine) and even in chatbots. 

It’s important to note that stemming algorithms are heuristic processes and they do not follow the language’s morphology strictly. 

They just remove and replace well-known suffixes of words to extract the base form.

### 1. PoterStemmer

It is not 100% accurate. It can change some words to different form.

```python
from nltk.stem import PorterStemmer

# PorterStemmer is a class. So have to make an Object

port_stemmer = PorterStemmer()
port_stemmer.stem(word)

# For List of words we can use for loop to iterate over it
words = ['eating', 'playable'] 

for i in words:
	print(port_stemmer.stem(i))
```

### 2. RegexpStemmer

Regular Expression Stemmer

```python
from nltk.stem import RegexpStemmer

# RegexpStemmer Requires Regex Expression & minimum legth of string to stem

regex_stemmer = RegexpStemmer('ing$|es$|s$|able$', min=4)
regex_stemmer.stem(word)

# For List of words we can use for loop to iterate over it
words = ['eating', 'playable', 'goes']

for i in words:
	print(regex_stemmer.stem(i))
```

### 3. Snowball Stemmer

It is somehow better than porter stemmer

```python
from nltk.stem import SnowballStemmer

# SnowballStemmerRequires Language

snow_stemmer = SnowballStemmer('english')
snow_stemmer.stem(word)

# For List of words we can use for loop to iterate over it
words = ['eating', 'playable', 'goes']

for i in words:
	print(snow_stemmer.stem(i))
```

## Example

```python

>>> from nltk.stem.snowball import SnowballStemmer
>>> snow_stemmer = SnowballStemmer('english')

>>> print(stemmer.stem("running"))
run

>>> print(stemmer.stem("having"))
have

```