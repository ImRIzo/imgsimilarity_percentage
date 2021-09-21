from flask import Flask, jsonify, request
from PIL import Image
import imgcompare

app = Flask(__name__)

@app.route('/compare', methods=['POST'])
def compare():
	uploaded_images = request.files.getlist('files[]')
	originalimage = Image.open(uploaded_images[0]).convert('L')
	comparelimage = Image.open(uploaded_images[1]).convert('L')
	differenceInPercentage = imgcompare.image_diff_percent(originalimage, comparelimage)
	accuracy = int(100 - differenceInPercentage)
	print(accuracy)
	return jsonify({'msg': 'success', 'accuracy': accuracy})

if __name__ == "__main__":
    app.run(debug=True)