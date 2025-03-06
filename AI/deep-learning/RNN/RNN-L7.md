
# Simple RNN

Here's a step-by-step tutorial for building a simple RNN for email spam classification using TensorFlow:

### 1. Import Required Libraries
```python
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
```

### 2. Load and Explore Data
```python
# Load dataset (example using SMS Spam Collection)
url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
df = pd.read_csv(url, sep='\t', names=['label', 'message'])

# Check first few rows
print(df.head())

# Check class distribution
print(df['label'].value_counts())
```

### 3. Data Preprocessing
```python
# Convert labels to binary values (spam=1, ham=0)
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    df['message'], 
    df['label'], 
    test_size=0.2, 
    random_state=42
)

# Text preprocessing parameters
vocab_size = 10000  # Number of words to keep
max_length = 100    # Maximum length of input sequences
trunc_type = 'post' # Truncate longer sequences at the end
padding_type = 'post' # Pad shorter sequences at the end
oov_tok = "<OOV>"   # Token for out-of-vocabulary words

# Initialize and fit tokenizer
tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
tokenizer.fit_on_texts(X_train)

# Convert texts to sequences
train_sequences = tokenizer.texts_to_sequences(X_train)
test_sequences = tokenizer.texts_to_sequences(X_test)

# Pad sequences
train_padded = pad_sequences(train_sequences, maxlen=max_length, 
                            padding=padding_type, truncating=trunc_type)
test_padded = pad_sequences(test_sequences, maxlen=max_length, 
                           padding=padding_type, truncating=trunc_type)
```

### 4. Build RNN Model
```python
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=vocab_size, 
                             output_dim=64, 
                             input_length=max_length),
    tf.keras.layers.SimpleRNN(64),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy', 
              optimizer='adam', 
              metrics=['accuracy'])

model.summary()
```

### 5. Train the Model
```python
history = model.fit(
    train_padded,
    y_train.values,
    epochs=5,
    validation_data=(test_padded, y_test.values),
    verbose=1
)
```

### 6. Evaluate Model Performance
```python
# Plot training history
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# Evaluate on test data
loss, accuracy = model.evaluate(test_padded, y_test)
print(f'Test Accuracy: {accuracy:.2f}')
```

### 7. Make Predictions
```python
def predict_spam(sample_text):
    # Preprocess input
    seq = tokenizer.texts_to_sequences([sample_text])
    padded = pad_sequences(seq, maxlen=max_length, 
                          padding=padding_type, truncating=trunc_type)
    # Predict
    prediction = model.predict(padded)[0][0]
    return 'Spam' if prediction > 0.5 else 'Ham'

# Test with sample messages
print(predict_spam("Congratulations! You've won a $1000 Walmart gift card."))
print(predict_spam("Hey, can we reschedule our meeting to tomorrow?"))
```

### Explanation of Key Components:
1. **Embedding Layer**: Converts word indices to dense vectors of fixed size (64-dimensional in this case)
2. **SimpleRNN Layer**: Basic recurrent layer that processes sequences with 64 units
3. **Dense Layer**: Output layer with sigmoid activation for binary classification
4. **Tokenizer**: Converts text to integer sequences
5. **Padding**: Ensures all input sequences have the same length

### Tips for Improvement:
- Try using LSTM/GRU layers instead of SimpleRNN
- Experiment with different embedding dimensions
- Add more layers or dropout for regularization
- Tune hyperparameters (batch size, number of epochs)
- Use pre-trained word embeddings like GloVe

This simple model should give you a good starting point (~85-90% accuracy) for spam classification. For production use, you'd want to add more sophisticated preprocessing and model tuning.