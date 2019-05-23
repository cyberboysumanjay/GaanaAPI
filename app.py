from flask import Flask, render_template,request,flash
import time
from flask import  jsonify,json
import gaana
app = Flask(__name__)
app.secret_key = 'test'

@app.route('/')
def home():
   return "Working"

@app.route('/result/')
def result():
    link=request.args.get('url')
    data=jsonify(gaana.downloadAndParsePage(link))
    print(data)
    return data

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=6000,use_reloader=True)
