from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import base64

def getImageLabels(image, imageType):
    app = ClarifaiApp(api_key='3d2bfbb7ebcc4598bbba8e3833a9b742')
    model = app.models.get('general-v1.3')

    result = None
    if imageType == 'base64':
        image = image.encode('ascii')
        result = model.predict([ClImage(base64=image)])
    elif imageType == 'url':
        result = model.predict([ClImage(url=image)])

    imageLabels = [];
    for concept in result["outputs"][0]["data"]["concepts"]:
        imageLabels.append(concept["name"])

    return imageLabels;

