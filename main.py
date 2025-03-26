import os, requests

from flask import Flask, render_template


app = Flask(__name__, template_folder='template', static_folder='static')

picFolder = os.path.join('static', 'pics')

app.config['UPLOAD_FOLDER'] = picFolder

quote = "Su gimtadieniu!"
author = "Andrius Kubilius"

@app.route("/")
def home():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'image.png.webp')
    return render_template("index.html", user_image=pic1, quote=quote, author=author)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
