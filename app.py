from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
  return "llama2 cfis 16 tokens"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
