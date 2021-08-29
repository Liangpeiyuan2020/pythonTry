import os,demo

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    try:
        sttr = demo.main2()
        return sttr
    except Exception as e:
        zz = str(e)
        aa=zz+"okkkkkkkkkkkkkktt"
        return aa

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
