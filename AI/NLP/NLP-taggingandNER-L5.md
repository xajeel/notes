# 5. Tagging & NER

Tagging, in the context of Natural Language Processing (NLP), refers to the process of assigning grammatical categories, or 'tags', to words in a text. 

This can include parts-of-speech (POS) tagging, where words are classified as nouns, verbs, adjectives, etc., as well as more complex tasks like named entity recognition (NER), where words are identified as names of people, organizations, locations, etc. 

Tagging is a crucial step in many NLP tasks, as it helps to understand the structure and meaning of the text.

```python
import nltk

# First Download Averaged Perceptron Tagger
nltk.download('averaged_perceptron_tagger')

tags = nltk.pos_tag(tokenized_words)
```

## Name Entity Recognition (NER)

Named Entity Recognition (NER) in NLP is a subtask of information extraction that seeks to locate and classify named entities in text into predefined categories such as person names, organizations, locations, medical codes, time expressions, quantities, monetary values, percentages, etc. 

This process can help answer many real-world questions, such as "Which companies were mentioned in the news article?", "Were specified products mentioned in complaints or reviews?", or "Does the tweet contain the name of a person? Does the article mention a city or country?".

```python
#In Python, NLTK library has a module, nltk.ne_chunk(), that can recognize named entities
import nltk
nltk.download('maxent_ne_chunker')
nltk.download('words')

tags = nltk.pos_tag(tokenized_words)
named_entities = nltk.ne_chunk(tags)

# To make a Graph

named_entities = nltk.ne_chunk(tags).draw()

```