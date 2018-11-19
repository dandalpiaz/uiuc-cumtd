from flask import Flask, render_template, request, send_from_directory
from flask_sslify import SSLify
import urllib.request, json 

app = Flask(__name__)
sslify = SSLify(app)

@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/manifest.json')
def static_from_root_1():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/logo.png')
def static_from_root_2():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/stop_id=<stop_id>/name=<name>')
def get_stop(stop_id, name):

	stop_data = "https://developer.cumtd.com/api/v2.2/json/GetDeparturesByStop?key=f43367cb918d4110af23345fff93f294&stop_id=" + stop_id + "&pt=60"
	
	try:
		with urllib.request.urlopen(stop_data, timeout=25) as url:
			data = json.loads(url.read().decode())
	except:
		return render_template('error.html')
		
	return render_template('stop.html', data=data, name=name)

if __name__ == '__main__':
    app.debug = False
    app.run()