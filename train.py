import tensorflow as tf
from keras_preprocessing.image import ImageDataGenerator

physical_devices = tf.config.experimental.list_physical_devices('GPU')

config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.compat.v1.Session(config=config)

# 90% accuracy


def save(cnn):
    cnn.save_weights("Model/weights.h5")
    model_json = cnn.to_json()
    with open("Model/model_json.json", "w") as json_file:
        json_file.write(model_json)


def data_preprocessing():
    train_datagen = ImageDataGenerator(
        rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
    valid_datagen = ImageDataGenerator(rescale=1. / 255)

    training_set = train_datagen.flow_from_directory(
        'dataset/training_set',
        target_size=(224, 224),
        batch_size=32,
        class_mode='binary')

    valid_set = valid_datagen.flow_from_directory(
        'dataset/valid',
        target_size=(224, 224),
        batch_size=32,
        class_mode='binary')

    return train_datagen, training_set, valid_datagen, valid_set


def train_model():
    train_datagen, training_set, test_datagen, test_set = data_preprocessing()

    cnn = tf.keras.models.Sequential()

    cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3,
                                   activation='relu', input_shape=[224, 224, 3]))
    cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

    cnn.add(tf.keras.layers.Conv2D(filters=64, kernel_size=3,
                                   activation='relu'))
    cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

    cnn.add(tf.keras.layers.Conv2D(filters=128, kernel_size=3,
                                   activation='relu'))
    cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))

    cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
    cnn.add(tf.keras.layers.Conv2D(filters=256, kernel_size=3,
                                   activation='relu'))

    cnn.add(tf.keras.layers.Flatten())
    cnn.add(tf.keras.layers.Dense(units=1, activation="sigmoid"))

    cnn.compile(optimizer="adam", metrics=[
                'accuracy'], loss="binary_crossentropy")

    cnn.fit(x=training_set, epochs=20, validation_data=test_set)

    save(cnn)


def main():
    train_model()


if __name__ == '__main__':
    main()
