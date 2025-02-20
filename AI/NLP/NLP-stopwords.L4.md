# 4. Stop Words

Stop words are commonly used words that a search engine has been programmed to ignore, both when indexing entries for searching and when retrieving them as the result of a search query.

In natural language processing, stop words are words which are filtered out before or after processing of text. 

When building the vocabulary of a text corpus, it is a good practice to consider removal of stop words. 

Examples of stop words include "a", "an", "the", "and", "in", and "is".

```python
from nltk.tokenize import word_tokenizer
from nltk.corpus import StopWords

# We need to download the list if Stop word from NLTK for Different Languages
import nltk
nltk.download('stopwords')

# To look at all the stop words in English
stop_words = stopwords.words('english')

# We Apply StopWords on the Tokenized Words
sentence = "This is a nlp notebook"
words = word_tokenizer(sentence)

new_list = []

for i in words:
	if i not in steo_words:
		new_list.append(i)

```