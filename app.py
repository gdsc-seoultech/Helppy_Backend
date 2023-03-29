from flask import Flask, jsonify, request
import base64
from easy_ocr_model import ocr_model

app = Flask(__name__)


@app.route("/img-src", methods=["POST"])
def hello():
  req = request.get_json()
  encoded_data = req["base64"]
  decoded_data = base64.b64decode(encoded_data)
  recognized_text = ocr_model(decoded_data)
  res = {
    "recognized_text": recognized_text,
  }
  res = jsonify(res)
  if recognized_text != "failed":
    return res, 200
  return jsonify({"recognized_text": "None"}), 401

if __name__ == '__main__':
  app.run('0.0.0.0', port=80)
