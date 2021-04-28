import pytest
from model.model import init, predict
from model.config import model_name, model_tags, model_type


@pytest.fixture(scope="session", autouse=True)
def initialize_model():
    """
    Before running any tests, we will initialize the model.
    """
    init()


def test_model_name():
    assert type(model_name) is str  # Make sure this is a string
    assert model_name.isidentifier()  # Ensure name is valid for sending via HTTP
    assert len(model_name) > 0  # Ensure name is non empty


def test_model_tags():
    assert type(model_tags) is list  # Make sure the tag list object is a list.
    assert len(model_tags) > 0  # Model must contain at least one tag
    for model_tag in model_tags:
        assert type(model_tag) is str  # Make sure tag is a string
        assert len(model_tag) > 0  # Ensure tag name is non empty


def test_model_type():
    assert type(model_type) is str  # Make sure this is a string
    assert model_type in ['image', 'text', 'video']  # Ensure type is valid
    assert len(model_type) > 0  # Ensure name is non empty


def test_predict_single_image():
    image_file = '1.png'
    prediction_result = predict(image_file)
    assert len(prediction_result.keys()) == 2  # Ensure correct size dict returned
    assert 'classes' in prediction_result and 'result' in prediction_result  # Ensure fields present

    # Ensure that the result classes are valid
    assert len(prediction_result['classes']) > 0
    for result_class in prediction_result['classes']:
        assert type(result_class) is str
        assert len(result_class) > 0

    # Ensure that the result values are valid
    valid_result_types = [str, int, float]
    for result_key in prediction_result['result'].keys():  # Ensure all values accounted for in class list
        assert result_key in prediction_result['classes']
        assert type(prediction_result['result'][result_key]) in valid_result_types


def test_bad_image_file():
    if model_type == 'image':
        with pytest.raises(FileNotFoundError):
            predict('iDoNotExist.txt')


def test_predict_multiple_images():
    """
    Test prediction on multiple images. Ensure that the classes returned are valid and that the
    results are consistent across all images.
    """

    for image_file_index in range(1, 6):
        image_file = str(image_file_index) + '.png'
        prediction_result = predict(image_file)
        assert len(prediction_result.keys()) == 2  # Ensure correct size dict returned
        assert 'classes' in prediction_result and 'result' in prediction_result  # Ensure fields present
        for result_key in prediction_result['result'].keys():  # Ensure all values accounted for in class list
            assert result_key in prediction_result['classes']
