# 1. Tokenization

We take a paragraph or sentence and then convert it into tokens. Tokens can be sentences or words.

**e.g.**

I am saim. I am a 23 years olds ( a paragraph )

After Tokenization it will change into tokens or sentences.

If the tokenziation is applied to sentences it will change into words.

- **Corpus** —- Paragraph of Text
- **Documents** —— Sentences of Text
- **Vocabulary** —— Unique Words in my Sentence
- **Words**

```python
!pip install nltk
```

```python
# Sentence Tokenizer
from nltk.tokenize import sent_tokenize
sent_tokenize(paragraph)

# Word tokenize
from nltk.tokenize import word_tokenize
word_tokenize(paragraph)

# we can also tokenize a sentence
word_tokenize(sentence)

# Both of these will return a List of words or sentences.
```