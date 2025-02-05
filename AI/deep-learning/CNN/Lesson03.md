# Using VGG16 for Cat vs Dog Classification in TensorFlow

This Lesson demonstrates how to use the pre-trained VGG16 model with a Sequential API for binary classification of cat and dog images.

**Please Check out the Implementation Files before coming to this Lesson**

[Custom Dataset Implementation](CNN_custom_dataset.md)

## Steps:
- Load and preprocess your dataset.
- Train the model using model.fit().
- Evaluate performance on test data.



```python
import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout, Conv2D, MaxPooling2D

# Load the pre-trained VGG16 model without the top classification layers
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Freeze the base model layers so they are not updated during training
base_model.trainable = False

# Create the Sequential model
model = Sequential()
model.add(base_model)
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))  # Binary classification (Cat vs Dog)

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Print the model summary
model.summary()
```