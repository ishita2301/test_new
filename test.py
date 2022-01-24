###dfddsmggsfdgsgggagvfgffdffsds#g#dfgtfgffgyg#h#ddf#gfgf##dgf###f#ffss#hfas##h#####kkkk#rgrr######
import pandas as pd
from flask import Flask,jsonify
from flask import request

# creating flask app
app = Flask(__name__)

@app.route('/python_script', methods = ('POST',))
def python_script():
    uid = request.form['uid']
    print(uid)
    mobile_no = request.form['mobile_no']
    print(mobile_no)
    return {"uid" : uid,"mobile_no":mobile_no}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8097)
    