# What are LSTMs?

**LSTM** stands for **Long Short-Term Memory**.
It's a type of **Recurrent Neural Network (RNN)**, designed to **remember patterns over long sequences** of data.

Imagine reading a book—your brain remembers what happened in the previous chapter. LSTMs try to do the same for data: they remember important information **from earlier steps** in a sequence to make **better predictions** later.

---

## Why Were LSTMs Introduced?

Standard RNNs could process sequences (like sentences or time series), but they had a **major problem**:

### The **vanishing gradient problem**

When training RNNs, the signal (or "gradient") gets weaker as it goes back through many steps.
This made it **very hard for RNNs to learn long-term dependencies** (e.g., remembering the subject of a sentence when predicting the verb).

**LSTMs were introduced in 1997** by Hochreiter and Schmidhuber to solve this.

---

## How Do LSTMs Fix This?

LSTMs use a **special structure called memory cells**, with **gates** that control the flow of information:

* **Forget Gate**: Decides what to forget from the past.
* **Input Gate**: Decides what new information to store.
* **Output Gate**: Decides what to send to the next step.

This makes them **great at keeping important information for a long time**, and ignoring what’s not important.

---

## Pros of LSTMs

1. **Can remember long sequences** of information.
2. **Solve vanishing gradient problem**, unlike regular RNNs.
3. Work well for:

   * Text (language modeling, machine translation)
   * Time series forecasting (e.g., stock prices)
   * Speech recognition

---

## Cons of LSTMs

1. **Complex**: More parameters and slower to train.
2. **Harder to parallelize**: Each step depends on the previous one.
3. **Outperformed by newer models** like Transformers (used in GPT, BERT).

---

## In Summary:

| Feature        | LSTM Explanation                       |
| -------------- | -------------------------------------- |
| Goal           | Learn from sequences over time         |
| Key Innovation | Memory cell with gates                 |
| Solves Problem | Long-term memory & vanishing gradients |
| Best For       | Language, time series, speech, etc.    |
| Limitation     | Complexity and training time           |

---

# LSTM 

Here's a beginner-friendly tutorial for building a simple LSTM model using TensorFlow for sentiment analysis on the IMDb movie reviews dataset:

---

### 1. Import Required Libraries
```python
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.datasets import imdb
import matplotlib.pyplot as plt
```

### 2. Load and Prepare Dataset
```python
# Parameters
vocab_size = 10000  # Keep top 10,000 most frequent words
max_length = 500    # Truncate/pad sequences to 500 words
padding_type = 'post'
trunc_type = 'post'

# Load IMDb dataset (already preprocessed)
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=vocab_size)

# Pad sequences to ensure uniform input length
train_data = pad_sequences(train_data, maxlen=max_length, padding=padding_type, truncating=trunc_type)
test_data = pad_sequences(test_data, maxlen=max_length, padding=padding_type, trunc_type=trunc_type)
```

### 3. Build LSTM Model
```python
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=vocab_size, 
                             output_dim=64, 
                             input_length=max_length),
    tf.keras.layers.LSTM(64),  # LSTM layer with 64 memory units
    tf.keras.layers.Dense(1, activation='sigmoid')  # Output layer for binary classification
])

model.compile(loss='binary_crossentropy', 
              optimizer='adam', 
              metrics=['accuracy'])

model.summary()
```

### 4. Train the Model
```python
history = model.fit(
    train_data,
    train_labels,
    epochs=5,
    validation_data=(test_data, test_labels),
    verbose=1
)
```

### 5. Evaluate Performance
```python
# Plot training history
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# Final evaluation
loss, accuracy = model.evaluate(test_data, test_labels)
print(f'\nTest Accuracy: {accuracy:.2f}')
```

### 6. Make Predictions
```python
# Get word index for text preprocessing
word_index = imdb.get_word_index()

def predict_sentiment(text):
    # Convert text to sequence of integers
    words = text.lower().split()
    sequence = [word_index.get(word, 2) for word in words]  # Use 2 for out-of-vocabulary words
    padded = pad_sequences([sequence], maxlen=max_length, 
                          padding=padding_type, truncating=trunc_type)
    prediction = model.predict(padded)[0][0]
    return 'Positive' if prediction > 0.5 else 'Negative'

# Test with sample reviews
print(predict_sentiment("This movie was fantastic! The acting was superb."))
print(predict_sentiment("Terrible film, would not recommend to anyone."))
```

---

### Key Components Explained:
1. **Embedding Layer**: 
   - Converts word indices (integers) into dense vectors of fixed size (64-dimensional here)
   - Learns meaningful word representations during training

2. **LSTM Layer**:
   - Processes sequences while maintaining long-term memory
   - 64 units = number of memory cells to capture patterns

3. **Padding**:
   - Ensures all input sequences have the same length (500 words here)
   - 'post' padding adds zeros at the end of shorter sequences

4. **Dense Layer**:
   - Output layer with sigmoid activation for binary classification (0=negative, 1=positive)

### Tips for Improvement:
- Add dropout layers to prevent overfitting
- Experiment with bidirectional LSTMs (`tf.keras.layers.Bidirectional`)
- Use pre-trained word embeddings (e.g., GloVe)
- Tune hyperparameters (batch size, number of LSTM units)
- Try different architectures (add more LSTM layers)

This basic model should achieve ~85% accuracy on the IMDb dataset. For production use, you'd want to add more sophisticated preprocessing and hyperparameter tuning.