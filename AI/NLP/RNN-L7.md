# RNN with Tensorflow

To create a simple Recurrent Neural Network (RNN) using TensorFlow, we'll use a dataset to train and test the model. Let's use the IMDB movie review dataset, which is commonly used for sentiment analysis (binary classification: positive or negative).

Here are the steps:

1. **Load and preprocess the dataset**
2. **Build the RNN model**
3. **Compile the model**
4. **Train the model**
5. **Evaluate the model**

Here's the complete code:

```python
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence

# Load the dataset
max_features = 10000  # Only consider the top 10,000 words
maxlen = 500  # Only consider the first 500 words of each movie review

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)

# Preprocess the dataset
x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)

# Build the RNN model
model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(max_features, 128, input_length=maxlen),
    tf.keras.layers.SimpleRNN(128, return_sequences=False),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train,
          epochs=10,
          batch_size=32,
          validation_split=0.2)

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)

print(f'Test Accuracy: {test_acc}')

# Making Prediction

import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.preprocessing.text import text_to_word_sequence
import numpy as np

def predict_sentiment(model, review, word_index, maxlen=500):
    """
    Predict the sentiment of a given movie review.
    
    Parameters:
        model: Trained Keras model.
        review: String, raw movie review text.
        word_index: Dictionary mapping words to their IMDB index.
        maxlen: Integer, maximum length of the review sequence.
    
    Returns:
        Sentiment prediction (0 = Negative, 1 = Positive)
    """
    # Tokenize and convert review to sequence
    words = text_to_word_sequence(review)
    sequence_data = [word_index[word] if word in word_index and word_index[word] < 10000 else 2 for word in words]
    
    # Pad sequence
    sequence_data = sequence.pad_sequences([sequence_data], maxlen=maxlen)
    
    # Predict sentiment
    prediction = model.predict(sequence_data)[0][0]
    
    # Convert prediction to label
    return "Positive" if prediction > 0.5 else "Negative"

# Load the IMDB word index
word_index = imdb.get_word_index()

# Example usage (after training the model):
# model should be the trained RNN model
test_review = "This movie was fantastic! The acting was great and the story was very engaging."
print(predict_sentiment(model, test_review, word_index))


```

### Explanation:

1. **Load and preprocess the dataset**:
    - We use the IMDB dataset, which is already included in TensorFlow/Keras.
    - `num_words=max_features` ensures that only the top 10,000 most frequently occurring words are used.
    - `sequence.pad_sequences` is used to ensure all sequences have the same length, padding shorter sequences and truncating longer ones.
2. **Build the RNN model**:
    - We use a `Sequential` model.
    - The `Embedding` layer maps the input integers (representing words) to dense vectors of fixed size (128 in this case).
    - The `SimpleRNN` layer processes the sequences. Here, we use 128 units.
    - The `Dense` layer with a `sigmoid` activation function outputs the binary classification result.
3. **Compile the model**:
    - The model uses the `adam` optimizer.
    - The loss function is `binary_crossentropy`, suitable for binary classification.
    - We track the `accuracy` metric.
4. **Train the model**:
    - We train the model for 10 epochs.
    - The batch size is 32.
    - We use 20% of the training data for validation.
5. **Evaluate the model**:
    - We evaluate the model on the test dataset and print the accuracy.

This simple RNN model should provide a decent performance for binary sentiment classification on the IMDB dataset. For better performance, you could consider using more complex architectures such as LSTM or GRU layers.