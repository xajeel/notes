# 3. Lemmatization

Lemmatization is a process in natural language processing where we reduce words to their base or root form. 

The output we get after lemmatization is ‘lemma’ which is the root word other than the root stem.

The main benefit of lemmatization is that it can group together different forms of the same word, thereby reducing redundancy and helping in text preprocessing tasks such as text mining and information retrieval.

Lemmatization is Slower than Stemming.

### WordNetLemmatize

NLTK provides WordNetLemmatize.

```python
from nltk.stem import WordNetLemmatizer

# WordNetLemmatizer is a class. So we have to make an object first.

lemma = WordNetLemmatizer()
lemma.lemmatize(word, pos='n')

# Posstage for the WordNetLemmatizer
"""
"n" = Noun
"v" = Verb
"a" = Adjective
"r" = Adverb
"""

# For the List of words

for i in words:
	print(lemma.lemmatize(i, pos='n'))
```

## Exmaple

```python
>>> from nltk.stem import WordNetLemmatizer

>>> lemma = WordNetLemmatizer()

>>> print(lemma.lemmatize('dogs'))
dog

>>> print(lemma.lemmatize('churches'))
church

>>> print(lemma.lemmatize('aardwolves'))
aardwolf

>>> print(lemma.lemmatize('abaci'))
abacus

>>> print(lemma.lemmatize('hardrock'))
hardrock

```