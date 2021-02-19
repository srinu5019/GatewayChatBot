from chatbot import chatbot
from flask import Flask, render_template, request, session
from flask_session import Session



app = Flask(__name__)
app.static_folder = 'static'
# Check Configuration section for more details
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    if (userText != "home") and ('context' in session):
        if session["context"]:
            session["context"] = session["context"]+"."+userText
        else:
            session["context"] = userText
    else:
        session["context"] = userText
    print("Key requested:", session["context"])
    key, result = chatbot.get_response(session["context"].lower())
    session["context"] = key
    if result:
        return result
    else:
        session["context"]=""
        return "Something went wrong; probably due to wrong option. Please reach out to <a href=\"mailto:SUPPORT.CCL@NCR.COM\">CCL support team</a><br>1.Go back home screen"

if __name__ == "__main__":
    app.run() 