### **Lesson Plan: Training a CNN on a Custom Dataset**  

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

# **1️⃣ Loading a Custom Dataset**  

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
import matplotlib.pyplot as plt

# Load dataset from directory
train_dir = "dataset/train"
test_dir = "dataset/test"

train_data = tf.keras.utils.image_dataset_from_directory(train_dir, image_size=(150, 150), batch_size=32)
test_data = tf.keras.utils.image_dataset_from_directory(test_dir, image_size=(150, 150), batch_size=32)

# Class names (dogs, cats)
class_names = train_data.class_names
print("Class labels:", class_names)

# Display some images
plt.figure(figsize=(8, 8))
for images, labels in train_data.take(1):  # Take one batch
    for i in range(9):  # Show first 9 images
        plt.subplot(3, 3, i+1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(class_names[labels[i]])
        plt.axis("off")
plt.show()
```

---

# **2️⃣ Data Augmentation**  

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

data_augmentation = tf.keras.Sequential([
    layers.RandomFlip("horizontal"),  # Flip images
    layers.RandomRotation(0.2),       # Rotate images
    layers.RandomZoom(0.2),           # Zoom in images
    layers.RandomContrast(0.2)        # Adjust contrast
])
```

📌 **Activity:** Show students how augmented images look different!  

```python
plt.figure(figsize=(8, 8))
for images, _ in train_data.take(1):
    for i in range(9):  
        augmented_image = data_augmentation(images[i])
        plt.subplot(3, 3, i+1)
        plt.imshow(augmented_image.numpy().astype("uint8"))
        plt.axis("off")
plt.show()
```

---

# **3️⃣ Splitting the Dataset**  

### **Why Split the Dataset?**  
✔ **Training Set** – Used for learning (80%)  
✔ **Validation Set** – Helps tune model parameters (10%)  
✔ **Test Set** – Final evaluation (10%)  

🎨 **Analogy:** Think of a student preparing for an exam:  
- 📖 **Studying** = Training Set  
- 📝 **Practice Tests** = Validation Set  
- 🎯 **Final Exam** = Test Set  

📌 **Splitting the Data in TensorFlow:**  

```python
train_size = 0.8
train_batches = int(len(train_data) * train_size)

train_dataset = train_data.take(train_batches)
val_dataset = train_data.skip(train_batches)  # Remaining 20% is validation data

print("Training batches:", len(train_dataset))
print("Validation batches:", len(val_dataset))
```

---

# **4️⃣ Building a CNN Model**  

**📌 CNN Architecture for Image Classification:**  

```python
from tensorflow.keras import layers, models

# Create CNN model
model = models.Sequential([
    layers.Rescaling(1./255),  # Normalize pixel values

    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    layers.MaxPooling2D(2, 2),

    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),

    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),

    layers.Flatten(),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.5),  # Prevent overfitting
    layers.Dense(2, activation='softmax')  # 2 classes (dogs, cats)
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Show model summary
model.summary()
```

---

# **5️⃣ Training and Evaluating the Model**  

### **📌 Training the Model:**  

```python
history = model.fit(train_dataset, validation_data=val_dataset, epochs=10)
```

### **📌 Evaluating on Test Data:**  

```python
test_loss, test_acc = model.evaluate(test_data)
print(f"Test accuracy: {test_acc:.4f}")
```

---

# **6️⃣ Making Predictions**  

```python
import numpy as np

# Take one batch of test images
for images, labels in test_data.take(1):
    predictions = model.predict(images)
    predicted_labels = np.argmax(predictions, axis=1)

    plt.figure(figsize=(8, 8))
    for i in range(9):
        plt.subplot(3, 3, i+1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(f"Pred: {class_names[predicted_labels[i]]}, Actual: {class_names[labels[i]]}")
        plt.axis("off")
    plt.show()
```

---

# **Conclusion 🎯**  
✔ We **loaded** a custom dataset of images.  
✔ We **augmented** the data for better generalization.  
✔ We **split** the dataset into training, validation, and test sets.  
✔ We **built and trained** a CNN for image classification.  
✔ We **evaluated and tested** the model's performance.  

---