from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route("/api", methods=["GET", "POST"])
def qa():
    data = {"how are you": "hi i am fine . thanks for asking"}
    if request.method == "POST":
        data = {"how are you": "hi i am fine . thanks for asking"}
        return jsonify(data)
    return jsonify(data)

app.run(debug=True)


