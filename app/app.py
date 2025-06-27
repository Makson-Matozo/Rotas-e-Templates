from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/onepiece")
def onepiece():
    return render_template("onepiece.html")

@app.route("/bleach")
def bleach():
    return render_template("bleach.html")

@app.route("/naruto")
def naruto():
    return render_template("naruto.html")

@app.route("/dragonball")
def dragonball():
    return render_template("dragonball.html")

if __name__ == "__main__":
    app.run(debug=True)
