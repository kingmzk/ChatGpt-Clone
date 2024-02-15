from flask import Flask, render_template, jsonify, request
from flask import Flask
from flask_pymongo import PyMongo
import openai



openai.api_key = ""

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/ChatGpt"
mongo = PyMongo(app)

@app.route('/')
def hello_world():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    # print(myChats)
    return render_template('index.html', myChats = myChats)


# @app.route("/api", methods=["GET", "POST"])
# def qa():
#     data = {"how are you": "hi i am fine . thanks for asking"}
#     if request.method == "POST":
#         # print(request.json)
#         question = request.json.get("question")
#         print(question)
#         chat = mongo.db.ChatGpt.chats.find({"question":question})
#         print(chat)
#         if chat:
#             data = {"result": f"{chat['answer']}"}
#             return jsonify(data)
#         data = {"result": f"Answer of {question}"}
#         return jsonify(data)
#     return jsonify(data)


@app.route("/api", methods=["GET", "POST"])
def qa():
    data = {"how are you": "hi i am fine . thanks for asking"}
    if request.method == "POST":
        question = request.json.get("question")
        print(question)
        chat = mongo.db.chats.find_one({"question": question})
        print(chat)
        if chat:
            data = {"result": chat['answer']}
        else:
            response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=question,
                    temperature=0.7,
                    max_tokens=256,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                    )
            print(response)
            data = {"question": question, "answer": response["choices"][0]["text"]}
            mongo.db.chats.insert_one({"question": question, "answer": response["choices"][0]["text"]})
            return jsonify(data)
    data = {"result": "Thank you! I'm just a machine learning model designed to respond to questions and generate text based on my training data. Is there anything specific you'd like to ask or discuss? "}
        
    return jsonify(data)



app.run(debug=True)


