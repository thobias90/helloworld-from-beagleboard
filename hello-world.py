from flask import Flask

app = Flask(__name__)

@app.route('/')
def Get_Hello():
    return "<h1>Hello World, from beagleboard!</h1>",200


app.run(host= '0.0.0.0')

