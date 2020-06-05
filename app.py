from flask import Flask, render_template, request, flash, redirect
import time
from flask import jsonify, json
import gaana
from traceback import print_exc
app = Flask(__name__)
app.secret_key = 'thisisasecretkeyforgaanaapiokbye!'


@app.route('/')
def home():
    return redirect("https://cyberboysumanjay.github.io/GaanaAPI/")


@app.route('/result/', methods=['GET', 'POST'])
def result():
    data = ''
    link = request.args.get('url')
    lyrics = False
    lyrics_ = request.args.get('lyrics')
    if lyrics_ and lyrics_.lower() != 'false':
        lyrics = True
    try:
        data = (gaana.downloadAndParsePage(link, lyrics))
        if len(data) > 0:
            return jsonify(data)
        raise ArithmeticError
    except Exception as e:
        errors = []
        error = {
            'status': False,
            'error': e
        }
        errors.append(error)
        return jsonify(errors)
    return data


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, use_reloader=True)
