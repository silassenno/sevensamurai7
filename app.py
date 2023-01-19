from flask import Flask, render_template
from flask_sqlachlemy

app = Flask("Hello World")
@app.route('/')
def index():
    return render_template('base.html')
@app.route('/about')
def about():
    return 'About 7 Samurai ToDos'

if __name__ == "__main__":
    app.run(debug=True, port=5000)
