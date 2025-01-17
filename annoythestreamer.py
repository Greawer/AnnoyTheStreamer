from flask import Flask, render_template, request, jsonify
from client import add_facememe, top_facememe_id, first_facememe, add_normalmeme, top_normalmeme_id, first_normalmeme
from datetime import datetime


app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
  return render_template('AnnoyTheStreamer.html')

@app.route('/handle_get', methods=['GET'])
def handle_get():
    if request.method == 'GET':
        top_text = "a"
        bottom_text = "a"
        print(top_text, bottom_text)
        return render_template('FaceMeme.html', variable="a") 

@app.route('/handle_put_facememe', methods=['PUT'])
def handle_put():
    if request.method == 'PUT':
        meme = first_facememe()
        return jsonify(meme)
    
@app.route('/handle_put_normalmeme', methods=['PUT'])
def handle_put2():
    if request.method == 'PUT':
        meme = first_normalmeme()
        print(meme)
        return jsonify(meme)
    
@app.route('/handle_post', methods=['POST'])
def handle_post():
    if request.method == 'POST':
        top_text_facememe = request.form['top_text_facememe']
        bottom_text_facememe = request.form['bottom_text_facememe']
        image_normalmeme = request.form['image_normalmeme']
        top_text_normalmeme = request.form['top_text_normalmeme']
        bottom_text_normalmeme = request.form['bottom_text_normalmeme']
        if image_normalmeme=="":
            add_facememe({
                "_id" : top_facememe_id()+1,
                "top_text" : top_text_facememe,
                "bottom_text" : bottom_text_facememe,
                "timestamp" : datetime.now(),
                "done" : "no"
            })
            return render_template('AnnoyTheStreamer.html')
        else:
            add_normalmeme({
                "_id" : top_normalmeme_id()+1,
                "image" : image_normalmeme,
                "top_text" : top_text_normalmeme,
                "bottom_text" : bottom_text_normalmeme,
                "timestamp" : datetime.now(),
                "done" : "no"
            })
            return render_template('AnnoyTheStreamer.html')
    else:
        return render_template('AnnoyTheStreamer.html')
    
@app.route('/FaceMeme')
def facememe():
    return render_template('FaceMeme.html')

@app.route('/NormalMeme')
def normalmeme():
    return render_template('NormalMeme.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=2137)    