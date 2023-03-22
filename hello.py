from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<div style=\"text-align: center;\"><h1>Hello from KodeKloud!</h1><p>Welcome to GCP DevOps Course.</p><p></p></div>"