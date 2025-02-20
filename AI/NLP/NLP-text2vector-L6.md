# 6. Text To Vector Techniques

Text to Vector techniques, also known as word embedding techniques, are crucial in the field of Natural Language Processing (NLP). 

These techniques involve converting text into numerical vectors which can be easily processed by machine learning algorithms.

Unique words in a sentence or corpus plays very important role in vectorization.

## 1. OneHot Encoding

### Advantages of One Hot Encoding

1. It is a simple and straightforward method for converting text to vectors.
2. It can easily handle categorical data, making it useful for a number of machine learning algorithms.
3. It doesn't require much computational resources, making it ideal for smaller datasets.

### Disadvantages of One Hot Encoding

1. It can result in high dimensionality if the dataset has many unique values, which can slow down machine learning algorithms.
2. It does not capture any semantic relationships between words, which can limit its effectiveness in NLP tasks.
3. It treats all words as equally distant, which may not be accurate in many NLP tasks.

![87029one_hot_encoding_demo.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/b1c5fb27-b2fb-48b6-8733-8e0c0a1c75d4/bda8913d-46b3-4982-ab31-e194c3d81264/87029one_hot_encoding_demo.png)

### Example Code

Here is a simple example of how to perform one hot encoding using Python's Scikit-learn library:

```python
from numpy import array
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

# define example
data = ['cold', 'cold', 'warm', 'cold', 'hot', 'hot', 'warm', 'cold', 'warm', 'hot']
values = array(data)

# integer encode
label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(values)

# binary encode
onehot_encoder = OneHotEncoder(sparse=False)
integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
onehot_encoded = onehot_encoder.fit_transform(integer_encoded)

print(onehot_encoded)
```

In this example, the strings 'cold', 'warm', and 'hot' are transformed into a binary vector representation. This can be useful when we want to perform machine learning on data that includes categorical data.

## 2. Bag of Words

### Bag of Words (BoW)

Bag of Words (BoW) is a popular text to vector conversion technique in NLP. It represents text, such as a sentence or a document, as the bag (multiset) of its words, disregarding grammar and even word order but keeping multiplicity.

The BoW model learns a vocabulary from all of the documents, then models each document by counting the number of times each word appears.

For example, consider the following two sentences:

**Sentence 1:** "The cat sat on the mat."
**Sentence 2:** "The mat sat on the cat."

In the BoW model, both sentences would have the exact same representation, even though their meanings are completely different.

### Advantages of Bag of Words

1. It is a simple and easy-to-understand method for converting text to vectors.
2. It can handle large datasets and is computationally efficient.
3. It is highly scalable and can be used for a wide range of datasets.

### Disadvantages of Bag of Words

1. It creates large and sparse vectors, which can be computationally expensive for large datasets.
2. It does not capture any semantic or syntactic relationships between words.
3. It does not account for the order of words, which can lead to loss of context and meaning.
4. Out of Vocabulary

### Example Code

```python
from sklearn.feature_extraction.text import CountVectorizer

# define the documents
docA = "The car is driven on the road"
docB = "The train ran on the tracks"

# create the Document Term Matrix
count_vectorizer = CountVectorizer(stop_words='english')
count_vectorizer = CountVectorizer()
sparse_matrix = count_vectorizer.fit_transform([docA, docB])

# OPTIONAL: Convert Sparse Matrix to Pandas Dataframe to see the word frequencies.
doc_term_matrix = sparse_matrix.todense()
df = pd.DataFrame(doc_term_matrix,
                  columns=count_vectorizer.get_feature_names_out(),
                  index=['docA', 'docB'])
print(df)

```

```python
from nltk.tokenize import word_tokenize
from collections import Counter

def bag_of_words(text):
    # Tokenize the text
    words = word_tokenize(text)

    # Count the word frequencies
    word_freq = Counter(words)

    return word_freq

text = "The quick brown fox jumps over the lazy dog"
print(bag_of_words(text))

```

## 3. TF - IDF ( Term Frequency - Inverse Document Frequency )

### TF-IDF (Term Frequency-Inverse Document Frequency)

TF-IDF is a statistical measure used to evaluate the importance of a word in a document, which is part of a larger corpus. 

It's used in information retrieval and text mining, and it works by increasing proportionally to the number of times a word appears in the document, but it's offset by the frequency of the word in the corpus, which helps to adjust for the fact that some words appear more frequently in general.

**For example,**

Consider a document containing 100 words wherein the word "apple" appears 3 times. The term frequency (TF) for "apple" is then (3/100) = 0.03. 

Now, assume we have 10 million documents and "apple" appears in 1000 of these. Then, the inverse document frequency (IDF) is calculated as log(10,000,000/1,000) = 4. 

Thus, the TF-IDF weight is the product of these quantities, which is (0.03 * 4) = 0.12.

**Formula**

**TF = [ No. of rep of the word in sentence / No. of words in a sentence ]**

**IDF = log [ NO. of sentence / No. of sentence containg the word ]**

**Weight = TF * IDF**

### Advantages of TF-IDF

1. TF-IDF reflects how important a word is to a document in a collection, which is especially beneficial for search engine optimization.
2. It can help differentiate documents based on keyword frequency, making it a powerful feature for many machine learning algorithms.
3. Unlike a simple word count, TF-IDF considers both the frequency of the word in the document and the frequency of the word across all documents, providing a more balanced view.
4. Word Importance is Getting captured

### Disadvantages of TF-IDF

1. TF-IDF assumes that all words are independent, which may not always hold true because the meaning of some words can depend on the presence of other words.
2. It does not capture the position in text, semantics, co-occurrences in different documents, which can lead to a loss of context and meaning.
3. It gives a high weightage to less frequent words, which may not always be desired as some common words may also be important.

### Example Code

```python
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# define the documents
docA = "The car is driven on the road"
docB = "The train ran on the tracks"

# create the tf-idf model
tfidf_vectorizer = TfidfVectorizer()

# apply the model to the documents
tfidf_matrix = tfidf_vectorizer.fit_transform([docA, docB])

# convert the matrix to a pandas dataframe for easier viewing
df = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf_vectorizer.get_feature_names_out(), index=['docA', 'docB'])

print(df)
```

```python
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Define the documents
docA = "The car is driven on the road"
docB = "The train ran on the tracks"

# Tokenize and remove stop words
stop_words = set(stopwords.words('english'))
tokenized_docA = [word for word in nltk.word_tokenize(docA) if word not in stop_words]
tokenized_docB = [word for word in nltk.word_tokenize(docB) if word not in stop_words]

# Create the tf-idf model
tfidf_vectorizer = TfidfVectorizer()

# Apply the model to the tokenized documents
tfidf_matrix = tfidf_vectorizer.fit_transform([' '.join(tokenized_docA), ' '.join(tokenized_docB)])

# Convert the matrix to a pandas dataframe for easier viewing
df = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf_vectorizer.get_feature_names_out(), index=['docA', 'docB'])

print(df)

```