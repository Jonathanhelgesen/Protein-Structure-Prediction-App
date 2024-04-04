from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow.keras.backend as K
import numpy as np
import pickle

app = Flask(__name__)
CORS(app)

# Need to reuse this function for loading the model


def masked_accuracy(y_true, y_pred):
    y_true = K.flatten(y_true)
    y_pred = K.flatten(K.argmax(y_pred, axis=-1))

    y_true = K.cast(y_true, 'int32')
    y_pred = K.cast(y_pred, 'int32')

    mask = K.cast(K.not_equal(y_true, 0), 'float32')
    correct_predictions = K.cast(K.equal(y_true, y_pred), 'float32') * mask
    accuracy = K.sum(correct_predictions) / K.sum(mask)
    return accuracy


# Load the models
custom_objects = {"masked_accuracy": masked_accuracy}

model_sst3 = load_model('sst3_model_040114_64es.h5',
                        custom_objects=custom_objects)
model_sst8 = load_model('sst8_model_040114_64es.h5',
                        custom_objects=custom_objects)

# Load the tokenizers
with open('amino_acid_tokenizer (2).pickle', 'rb') as handle:
    seq_tokenizer = pickle.load(handle)

with open('sst3_tokenizer (1).pickle', 'rb') as handle:
    sst3_tokenizer = pickle.load(handle)

with open('sst8_tokenizer (1).pickle', 'rb') as handle:
    sst8_tokenizer = pickle.load(handle)

max_length = 400


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    sequence = data.get("sequence", "")

    # Encode the input sequence
    encoded_sequence = seq_tokenizer.texts_to_sequences([sequence])
    padded_sequence = pad_sequences(
        encoded_sequence, maxlen=max_length, padding='post')

    # Predict structures using both models
    prediction_sst3 = model_sst3.predict(padded_sequence)
    prediction_sst8 = model_sst8.predict(padded_sequence)

    # Decode the predictions to structure labels
    predicted_sst3_indices = np.argmax(prediction_sst3, axis=-1)[0]
    predicted_sst8_indices = np.argmax(prediction_sst8, axis=-1)[0]

    predicted_sst3_structure = ' '.join(
        [sst3_tokenizer.index_word.get(i, '') for i in predicted_sst3_indices if i > 0])
    predicted_sst8_structure = ' '.join(
        [sst8_tokenizer.index_word.get(i, '') for i in predicted_sst8_indices if i > 0])

    return jsonify({
        "predicted_sst3_structure": predicted_sst3_structure,
        "predicted_sst8_structure": predicted_sst8_structure
    })


if __name__ == '__main__':
    app.run(debug=True)
