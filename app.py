from flask import Flask, render_template,request,flash,redirect
import time
from flask import  jsonify,json
import gaana
from traceback import print_exc
app = Flask(__name__)
app.secret_key = 'test'

@app.route('/')
def home():
   return redirect("https://cyberboysumanjay.github.io/GaanaAPI/")

@app.route('/result/', methods=['GET', 'POST'])
def result():
    data=''
    link=request.args.get('url')
    try:
        data=(gaana.downloadAndParsePage(link))
        if len(data)>0:
            return jsonify(data)
        raise ArithmeticError
    except Exception as e:
        errors=[]
        error = {'title' : 'Unable to fetch',
                'album' : 'Unable to fetch',
                'thumb' : 'Unable to fetch',
                'language' : 'Unable to fetch',
                'gaana_url' : 'Unable to fetch',
                'duration' : 'Unable to fetch',
                'artist' : 'Unable to fetch',
                'released' : 'Unable to fetch',
                'bitrate' : 'Unable to fetch',
                'link' : 'Unable to fetch',
                'status': e
        }
        errors.append(error)
        return jsonify(errors)
    return data

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000,use_reloader=True)
