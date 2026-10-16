
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Shaik is testing the compilation</h1>
    <p>Python application is running successfully!</p>
    <p>Ready for deployment.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
