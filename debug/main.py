from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import logging
import traceback

app = FastAPI()
logger = logging.Logger(app)


init_status = 'Not Started.'
init_error = ''

predict_status = 'Not Started.'
predict_error = ''
predict_result = ''


def attempt_init():
    global init_status, init_error
    try:
        init_status = 'In Progress...'
        from model.model import init
        init()
        init_status = 'Successful'
        init_error = ''
    except:
        init_status = 'failed'
        init_error = traceback.format_exc()


def attempt_predict():
    global predict_status, predict_error, predict_result
    try:
        predict_status = 'In Progress...'
        from model.model import predict
        predict_result = predict('COCO_val2014_000000581394.jpg')
        # predict_result = predict('COCO_val2014_000000488977.jpg')
        predict_status = 'Successful'
        predict_error = ''
    except:
        predict_status = 'failed'
        predict_result = ''
        predict_error = traceback.format_exc()


@app.on_event('startup')
def on_startup():
    attempt_init()
    attempt_predict()


@app.get("/", response_class=HTMLResponse)
async def show_overview():
    html_content = """
    <html>
        <head>
            <title>Model Debug Status</title>
            <style>
                .errorCode {
                    font-family: 'Courier New', monospace;
                    color: red;
                    width: 70vw;
                    border: 1px solid black;
                }
            </style>
        </head>
        <body>
            <h1>Model Debugging Utility</h1>
            <br>
            <h3>Initialization Status</h3>
            <p>%s</p>
            <p class="errorCode">%s</p>
            <br>
            <h3>Prediction Status</h3>
            <p>%s</p>
            <code>%s</code>
            <br> <br>
            <p class="errorCode">%s</p>
        </body> 
    </html>
    """ % (init_status, init_error, predict_status, predict_result, predict_error)
    return HTMLResponse(content=html_content, status_code=200)
