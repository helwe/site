import random
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def main():
    return render_template('HTMLmain.html')
@app.route('/me')
def price():
    return render_template('HTML.html')
@app.route('/weather')
def weather():
    temp=random.randint(-50,50)
    return render_template('HTMLweather.html',temp=temp)
app.run(debug=True)