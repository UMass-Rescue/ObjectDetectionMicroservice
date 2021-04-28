# Model Design Template

This model is designed accoding to the template in [UniversalModelTemaplate](https://github.com/UMass-Rescue/UniversalModelTemplate). The model passes the test cases in this application, and should work in
the context of the server.

## Getting Started
In the model directory, the code in `model.py` uses the pretrained [FasterRCNN](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/faster_rcnn.html) model in PyTorch to detect objects with prediction scores greater than **0.75**. This model is trained on the MS-COCO dataset with has [80 classes](https://cocodataset.org/#explore)  of objects (excluding background).
In `model/coco_labels_super.json`, the classes are grouped into 10 super-classes:- *person*, *modes of transport*, *street view*, *animals*, *sports*, *food*, *kitchen*, *indoor*, *electronis*, and *misc*. 
`config.py` has some metadata about the ML model, e.g. input type, model name, and tags. The requirements are added to `requirements.py` file in the model directory. 


## Debugging your Model

If you need extra information on how your model is performing, a built-in debugging server is provided
which will connect to the Docker container the model is running in and return error messages.

If you would like to use this, in the root directory of the project, run the command 
`docker-compose build debug` and then `docker-compose up debug`. Open a web browser and navigate to
[http://localhost:4650]('http://localhost:4650').

As you make changes to your model the results will appear on the web page showing the initialization
status and a prediction result on a test image.


## Testing your Model

In the root directory of the project, run the command `docker-compose build test` and then
`docker-compose up test`. You will see the results of the test cases in your terminal. If all
test cases pass, then your model will work in the server environment.
