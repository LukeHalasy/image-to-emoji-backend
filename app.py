from flask import Flask, jsonify, request 
from flask_cors import CORS, cross_origin
from getImageLabels import getImageLabels
from emojiFinder import getEmojis

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['POST'])
@cross_origin()
def apihomepage():
    data = request.get_json()

    image = None
    if 'image' in data:
        # Get rid of the type-define text of the request
        image = data['image']
        image = image.split(",")[1]

        # Get the labels of the image with clarify
        imageLabels = getImageLabels(image)

        # Get related emojis to the labels
        emojis = getEmojis(imageLabels)
        return jsonify(emojis=list(emojis), hashtags=["#" + hashtag for hashtag in imageLabels[0:5]])
    else:
        return 'Please send an image'

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True) 
