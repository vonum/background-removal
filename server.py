from typing import Optional
import urllib
import tempfile

from fastapi import FastAPI
from pydantic import BaseModel

import image_background_removal as ibrm

app = FastAPI()

MODELS = ["u2net", "u2netp", "basnet", "xception_model", "mobile_net_model"]
PREPROCESSING = ["bdd-fastrcnn", "bbmd-maskrcnn", "None"]
POSTPROCESSING = ["rtb-bnb", "rtb-bnb2", "No"]

IMAGE_URL = "https://upload.wikimedia.org/wikipedia/commons/1/1a/Donkey_in_Clovelly%2C_North_Devon%2C_England.jpg"

class ImageRequest(BaseModel):
    url: str
    model: Optional[str] = "u2net"
    preprocessing: Optional[str] = "bdd-fastrcnn"
    postprocessing: Optional[str] = "rtb-bnb"

@app.post("/remove_background")
async def root(image_request: ImageRequest):
    _validate_parameter("Model", image_request.model, MODELS)
    _validate_parameter("Preprocessing", image_request.preprocessing, PREPROCESSING)
    _validate_parameter("Postprocessing", image_request.postprocessing, POSTPROCESSING)

    output_path = _image_output_path()
    input_path = _image_input_path()

    urllib.request.urlretrieve(image_request.url, input_path)

    print(output_path)

    print(image_request.model)
    print(image_request.preprocessing)
    print(image_request.postprocessing)

    ibrm.process(input_path, output_path,
                 image_request.model,
                 image_request.preprocessing,
                 image_request.postprocessing)
    return {"message": "Hello World"}

def _validate_parameter(parameter, value, valid_values):
    if value not in valid_values:
        raise ValueError(f"{parameter} {value} is not valid.")

def _image_output_path():
    return f"{tempfile.mkdtemp()}/output.png"

def _image_input_path():
    return f"{tempfile.mkdtemp()}/input.png"
