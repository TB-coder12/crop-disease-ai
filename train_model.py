from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.optimizers import Adam
train_dir = 'dataset/train'
train_datagen = ImageDataGenerator(
rescale=1./255,
validation_split=0.2
)
train_data = train_datagen.flow_from_directory(
train_dir,
target_size=(224, 224),
batch_size=32,
class_mode='categorical',
subset='training'
)
val_data = train_datagen.flow_from_directory(
train_dir,
target_size=(224, 224),
batch_size=32,
class_mode='categorical',
subset='validation'
)
base_model = MobileNetV2(
input_shape=(224, 224, 3),
include_top=False,
weights='imagenet'
)
base_model.trainable = False
model = Sequential([
base_model,
Flatten(),
Dense(128, activation='relu'),
Dense(train_data.num_classes, activation='softmax')
  ])
model.compile(
optimizer=Adam(),
loss='categorical_crossentropy',
metrics=['accuracy']
)
model.fit(train_data, validation_data=val_data, epochs=5)
model.save('disease_model.h5')
labels = list(train_data.class_indices.keys())
with open('labels.txt', 'w') as f:
for item in labels:
f.write(item + '\n')
