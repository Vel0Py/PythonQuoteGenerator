import os, requests

from flask import Flask, render_template

url = 'http://api.quotable.io/random'

app = Flask(__name__, template_folder='template', static_folder='static')

picFolder = os.path.join('static', 'pics')

app.config['UPLOAD_FOLDER'] = picFolder


@app.route("/")
def home():
    r = requests.get(url)
    quote = r.json()
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'image.png.webp')
    return render_template("index.html", user_image=pic1, quote=quote['content'], author=quote['author'])


if __name__ == "__main__":
    app.run(debug=True)
