# **Training a CNN on a Custom Dataset**  

---

### **Lesson Objectives**  
By the end of this lesson, students will learn:  
✅ How to load a **custom image dataset** in TensorFlow  
✅ How to apply **data augmentation** to improve performance  
✅ How to **split the dataset** into training, validation, and test sets  
✅ How to build a **CNN model** for the custom dataset  
✅ How to **train the model** and evaluate its performance  

---

## **Lesson Outline**  

### **1️⃣ Loading a Custom Dataset**  
- Introduction to image datasets  
- Using `ImageDataGenerator` and `tf.keras.utils.image_dataset_from_directory`  

### **2️⃣ Data Augmentation**  
- Why data augmentation is important  
- Different augmentation techniques  

### **3️⃣ Splitting the Dataset**  
- Why we need **training, validation, and test sets**  
- How to split data using TensorFlow  

### **4️⃣ Building a CNN Model**  
- Creating a CNN using `Conv2D`, `MaxPooling2D`, and `Dense` layers  

### **5️⃣ Training and Evaluating the Model**  
- How to train the CNN  
- How to check accuracy and loss  
- Making predictions  

---

## **1️⃣ Loading a Custom Dataset**  

### **Why Do We Need a Custom Dataset?**  
MNIST contains handwritten digits, but real-world problems involve different kinds of images. Suppose we want to build a model to classify **dogs vs. cats**—we need to load a dataset containing **dog** and **cat** images.  

🎨 **Analogy:** Think of a CNN as a **student learning from examples**. If we want it to recognize dogs and cats, we must **provide images** of both!  

---

### **📌 Loading the Dataset**  
We'll assume we have a dataset with two folders:  
📂 `dataset/`  
- 📁 `train/`  
  - 📁 `dogs/` 🐶  
  - 📁 `cats/` 🐱  
- 📁 `test/`  
  - 📁 `dogs/`  
  - 📁 `cats/`  

**TensorFlow Code to Load Images:**  

```python
import tensorflow as tf

data_dir = '/content/1/training_set/training_set'

# Class names (dogs, cats)
class_names = train_data.class_names
print("Class labels:", class_names)

```

```python

train_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=(150, 150),
  batch_size=32)

val_ds  = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=(150, 150),
  batch_size=32)

class_names = train_ds.class_names
print(class_names)
```

---

## **2️⃣ Data Augmentation**  

### **What is Data Augmentation?**  
📌 Data augmentation **creates new variations** of images to improve model learning.  

🎨 **Analogy:** If a student only sees one style of handwriting, they might struggle with new handwriting styles. Data augmentation **teaches the CNN different styles!**  

**Common Augmentation Techniques:**  
✅ **Flipping** – Mirror images horizontally  
✅ **Rotation** – Rotate images slightly  
✅ **Zooming** – Zoom in on objects  
✅ **Brightness Change** – Simulate different lighting  

**TensorFlow Code for Data Augmentation:**  

```python
from tensorflow.keras import layers

for image_batch, labels_batch in train_ds:
  print(image_batch.shape)
  print(labels_batch.shape)
  break

data_augmentation = tf.keras.Sequential([
    layers.RandomFlip("horizontal"),  # Flip images
    layers.RandomRotation(0.2),       # Rotate images
    layers.RandomZoom(0.2),           # Zoom in images
    layers.RandomContrast(0.2)        # Adjust contrast
])
```

Normalizing the Images

```python
normalization_layer = tf.keras.layers.Rescaling(1./255)
normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
image_batch, labels_batch = next(iter(normalized_ds))
```

---

## **4️⃣ Building a CNN Model**  

**📌 CNN Architecture for Image Classification:**  

```python
from tensorflow.keras import layers, models

# Create CNN model


model = tf.keras.Sequential([
  tf.keras.layers.Rescaling(1./255),
  tf.keras.layers.Conv2D(32, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Conv2D(32, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Conv2D(32, 3, activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dense(2)
])

# Compile the model
model.compile(
  optimizer='adam',
  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=['accuracy'])

# Show model summary
model.summary()
```

---

## **5️⃣ Training and Evaluating the Model**  

### **📌 Training the Model:**  

```python
model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=3
)
```

### **📌 Evaluating on Test Data:**  

```python
test_loss, test_acc = model.evaluate(test_data)
print(f"Test accuracy: {test_acc:.4f}")
```

---

## **Conclusion 🎯**  
✔ We **loaded** a custom dataset of images.  
✔ We **augmented** the data for better generalization.  
✔ We **split** the dataset into training, validation, and test sets.  
✔ We **built and trained** a CNN for image classification.  
✔ We **evaluated and tested** the model's performance.  

---