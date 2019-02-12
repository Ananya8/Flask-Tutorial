from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/despacito")
def despacito():
    return "I am Illumanti/Despacito"
 
if __name__ == "__main__":
    app.run()
