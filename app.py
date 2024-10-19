from flask import Flask

import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Your full name
    full_name = "kriti raju"  # Replace with your name

    # Get the system username
    username = os.getlogin()

    # Get the current server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # Get the top command output
    top_output = subprocess.getoutput('top -b -n 1')

    # Generate the HTML content
    response = f"""
    <html>
        <head><title>HTop Info</title></head>
        <body>
            <h1>HTop Information</h1>
            <p><strong>Name:</strong> {full_name}</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time (IST):</strong> {server_time}</p>
            <h2>Top Command Output:</h2>
            <pre>{top_output}</pre>
        </body>
    </html>
    """
    return response

if __name__ == '__main__':
    app.run(debug=True)