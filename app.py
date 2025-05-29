from flask import Flask, render_template, request, redirect
import csv
from datetime import datetime

app = Flask(__name__)

# Home page – invitation
@app.route('/')
def home():
    return render_template('index.html')

# Handle vote submission
@app.route('/vote', methods=['POST'])
def vote():
    choice = request.form['location']
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Save the vote
    with open('votes.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, choice])

    return render_template('thankyou.html', choice=choice)

if __name__ == '__main__':
    app.run(debug=True)
