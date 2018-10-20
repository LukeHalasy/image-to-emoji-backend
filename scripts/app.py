from flask import Flask, request 
from getImageLabels import getImageLabels
from emojiFinder import getEmojis

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def test():
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
        return ', '.join(list(emojis))

if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000
