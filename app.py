from flask import Flask, render_template,request,flash
import time
from flask import  jsonify,json
import gaana
from traceback import print_exc
app = Flask(__name__)
app.secret_key = 'test'

@app.route('/')
def home():
   return "Working"

@app.route('/result/')
def result():
    data=''
    link=request.args.get('url')
    try:
        data=jsonify(gaana.downloadAndParsePage(link))
        return data
    except Exception as e:
        print(e)
        print_exc()
    #print(data)
    return data

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000,use_reloader=True)
