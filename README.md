## Object Detection Microservice

This model is designed accoding to the template in [UniversalModelTemaplate](https://github.com/UMass-Rescue/UniversalModelTemplate). The model passes all the test cases in this application, and should work in the context of the server.

In the model directory, the code in `model.py` uses the pretrained [FasterRCNN](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/faster_rcnn.html) model in PyTorch to detect objects with prediction scores greater than **0.75**. 

This model is trained on the MS-COCO dataset which has [80 classes](https://cocodataset.org/#explore)  of objects (excluding background).
In `model/coco_labels_super.json`, these classes are grouped into 10 super-classes. The model returns the number of objects detected in each of the super-classes. 

Super-class         | COCO Class Label
------------------- | -------------
person              | person
modes of transport  | bicycle, car, motorcycle, airplane, bus, train, truck, boat
street view         | traffic light, fire hydrant, stop sign, parking meter, bench
animals             | bird, cat, dog, horse, sheep, cow, elephant, bear, zebra, giraffe
sports              | frisbee, skis, snowboard, sports ball, kite, baseball bat, baseball glove, skateboard, surfboard, tennis racket
food                | banana, apple, sandwich, orange, broccoli, carrot, hot dog, pizza, donut, cake
kitchen             | wine glass, cup, fork, knife, spoon, bowl
indoor              | couch, potted plant, bed, dining table, toilet, sink, clock, vase
electronis          | tv, laptop, mouse, remote, keyboard, cell phone, microwave, oven, toaster, refrigerator, hair drier
misc                | book, scissors, teddy bear, toothbrush, tie, backpack, umbrella, handbag, suitcase, chair, bottle

**It is sufficient to make any required modifications or regrouping of the class labels in the JSON file itself. Everywhere else the changes would follow.**

`config.py` has some metadata about the ML model, e.g. input type, model name, and tags. 
The requirements are added to `requirements.py` file in the model directory. 


## Debugging your Model

In the root directory of the project, run the command 
`docker-compose build debug` and then `docker-compose up debug`. Open a web browser and navigate to
[http://localhost:4650]('http://localhost:4650').

As you make changes to your model the results will appear on the web page showing the initialization
status and a prediction result on a test image.


## Testing your Model

In the root directory of the project, run the command `docker-compose build test` and then
`docker-compose up test`. You will see the results of the test cases in your terminal. If all
test cases pass, then your model will work in the server environment.
