from flask import Flask, render_template, request, redirect, url_for, make_response
import motors
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

app = Flask(__name__) #set up flask server

#when the root IP is selected, return index.html page
@app.route('/')
def index():
        return render_template('index.html')

#recieve pin change from the button press on index.html
#each button returns a number that triggers a command in this function
@app.route('/<changepin>', methods=['POST'])
def reroute(changepin):

	changePin = int(changepin) #cast changepin to an int

	if changePin == 1:
		motors.turnLeft()
	elif changePin == 2:
		motors.forward()
	elif changePin == 3:
		motors.turnRight()
	elif changePin == 4:
		motors.backward()
	else:
		motors.stop()

	response = make_response(redirect(url_for('index')))
	return(response)

app.run(debug=True, host='0.0.0.0', port=8000) #set up the server in debug mode to the port 8000
