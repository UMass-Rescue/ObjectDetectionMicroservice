# Model Design Template

This template was created to speed up the model design and development process.
If the model passes the test cases in this application, then it will also work in
the context of the server.

## Getting Started
In the model directory, fill out the code in `model.py` and `config.py` according to
the directions in each file. Then, add the requirements for your project into the
`requirements.py` file in the model directory. You may add any supporting files or
folders that your model needs under the model directory.

**Important: All code that your model uses or references *MUST* be contained in the
model directory.**


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