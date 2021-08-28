import os,demo

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    try:
        sttr = demo.main2()
        saar = sttr[0]
        saar = str(saar)+"niubi"
        return saar
    except Exception as e:
        zz = str(e)
        aa = zz + "fffffffffffffffffffff"
        return aa

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
