import tensorflow as tf
from tensorflow.keras.models import model_from_json
from tensorflow.keras.optimizers import RMSprop

config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.compat.v1.Session(config=config)


class Loader:
    def __init__(self):
        print("Initialized loader")

    def load(self):
        json_model = open("model_json.json", "r")
        loaded_model_js = json_model.read()
        json_model.close()
        model = model_from_json(loaded_model_js)
        model.load_weights("weights.h5")
        model.compile(loss='categorical_crossentropy',
                      optimizer="adam", metrics=['accuracy'])
        return model
