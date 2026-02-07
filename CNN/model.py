from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models

IMG_SIZE = 64
BATCH_SIZE = 8

datagen = ImageDataGenerator(
    rescale=1./255,
    brightness_range=(0.7, 1.3),
    rotation_range=3,
    validation_split=0.2
)


train_data = datagen.flow_from_directory(
    "dataset",
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="training"
)

val_data = datagen.flow_from_directory(
    "dataset",
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="validation"
)

model = models.Sequential([
    layers.Conv2D(32, (3,3), activation="relu", input_shape=(64,64,3)),
    layers.MaxPooling2D(),

    layers.Conv2D(64, (3,3), activation="relu"),
    layers.MaxPooling2D(),

    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dense(train_data.num_classes, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

model.fit(train_data, validation_data=val_data, epochs=30)

model.save("gesture_cnn.keras")
