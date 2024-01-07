#!/usr/bin/env python
import os
from flask import Flask, render_template
import datetime

app = Flask(__name__)


# Function to get the current time of the day
def get_time_of_day():
    current_time = datetime.datetime.now()
    hour = current_time.hour

    if 5 <= hour < 12:
        return "morning"
    elif 12 <= hour < 17:
        return "afternoon"
    else:
        return "evening"


# Route for the home page
@app.route('/')
def home():
    # Get the time of the day
    time_of_day = get_time_of_day()

    # Replace 'Your Name' with your actual name
    name = "giorgosbour"

    # Render the template with the personalized greeting
    return render_template('index.html', time_of_day=time_of_day, name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)