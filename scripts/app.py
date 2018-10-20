from flask import Flask, request 
from getImageLabels import getImageLabels

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def test():
    data = request.get_json()

    image = None
    if 'image' in data:
        image = data['image']
        image = image.split(",")[1]
        return getImageLabels(image)

if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000
