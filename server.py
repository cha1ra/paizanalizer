from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask import Response

from module import paiza
import ast




def get_data():
    data_path = 'data/data_dict.txt'
    try:
        with open(data_path) as f:
            s = f.read()
            return ast.literal_eval(s)
    except:
        return None


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def paizanalizer():
    if request.method == 'GET':
        data = get_data()
        return render_template('index.php', data = data)
    elif request.method == 'POST':
        paiza.get_data(request.form['mail'],request.form['pass'])
        data = get_data()
        return render_template('index.php', data = data)

def main():
    app.debug = True
    app.run(host='127.0.0.1', port=5000)


if __name__ == '__main__':
    main()