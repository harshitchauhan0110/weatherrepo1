from flask import Flask , request , render_template
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/weatherapp', methods = ['POST' , 'GET'])
def show_data():
    url = 'https://api.openweathermap.org/data/2.5/weather'
    param = {
        'q' : request.form.get('city'),
        'units' : request.form.get('units'),
        'appid' : request.form.get('appid')}
    response = requests.get(url,params = param)
    data = response.json()
    return f'data : {data}'

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5003)