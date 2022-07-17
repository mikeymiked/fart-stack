from flask import Flask, render_template, jsonify
import redis

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['FLASK_ENV'] = 'development'

@app.route('/')
def index():
    return render_template('index.html')

# r = redis.Redis(host='172.17.0.4', port=6379, db=0)
#first = r.get('firstname')
#last = r.get('lastname')

r = None

@app.route('/proof')
def proof():
    try:
        r = redis.Redis(host='redis.default.svc.cluster.local', port=6379, db=0)
    except:
        pass
    data = {
        'firstname': "{}".format(r.get('firstname').decode()),
        'lastname': "{}".format(r.get('lastname').decode()),
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
