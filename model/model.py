from typing import List

from PIL import Image
import time


def init():
    """
    This method will be run once on startup. You should check if the supporting files your
    model needs have been created, and if not then you should create/fetch them.
    """
    # Placeholder init code. Replace the sleep with check for model files required etc...
    time.sleep(1)


def predict(prediction_input):
    """
    Interface method between model and server. This signature must not be
    changed and your model must be able to create a prediction from the image
    file or text that is passed in.

    Depending on the model type as defined in model/config.py, this method will receive a different input:

    'image'  :  Model receives a file name to an image file, opens it, and creates a prediction
    'text'   :  Model receives a string of text and uses it to create a prediction.


    Note: All images are stored in the directory '/app/images/' in the Docker container. You may assume that the file
    name that is passed to this method is valid and that the image file exists.

    Example code for opening the image using PIL:
    image = Image.open('/app/images/'+image_file_name)
    """

    text_input = prediction_input  # If text model
    image = Image.open('/app/images/' + prediction_input)  # If image model

    return {
        'classes': ['isGreen', 'isRed'],  # List every class in the classifier
        'result': {  # For results, use the class names above with the result value
            'isGreen': 0,
            'isRed': 1
        }
    }


def predict_batch(prediction_inputs: List[str]):
    """
    Create a batch prediction. This should have the same functionality as the predict function, however it
    will allow for any optimizations.

    This will be passed prediction inputs of length "batch_size", configurable in the model/config.py
    batch_size variable.

    If your model does not support batch prediction, you may disregard this method and your model will
    still be completely functional.

    The return signature for this message is a dictionary, with each key being the name of a prediction input in
    prediction_inputs, and each value being the same format as what is returned in the singular predict() method.

    """

    results = {}

    # This is a placeholder if your code does not have any batch optimizations.
    for prediction_input in prediction_inputs:
        results[prediction_input] = predict(prediction_input)

    return results
