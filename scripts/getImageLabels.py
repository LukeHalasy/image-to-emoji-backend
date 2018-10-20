from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import base64

def getImageLabels(base64Img):
    app = ClarifaiApp(api_key='3d2bfbb7ebcc4598bbba8e3833a9b742')
    model = app.models.get('general-v1.3')
    base64Img = base64Img.encode('ascii')
    result = model.predict([ClImage(base64=base64Img)])
    imageLabels = [];
    for concept in result["outputs"][0]["data"]["concepts"]:
        imageLabels.append(concept["name"])

    return imageLabels;

