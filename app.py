from flask  import Flask,render_template,request,jsonify
from core  import get_bot_response
from os import environ

#creating flask name
app = Flask(__name__,static_folder='static',template_folder='templates')
#main web page
@app.route('/')
def home():
    return render_template("index.html")
#loading templetes/index.html

#message hundling
@app.route('/chat', methods =["POST"])
def chat():
    data = request.get_json()
    user_message = data.get('message','')

    bot_reply =get_bot_response(user_message) #passes it to core.py
    return jsonify({'reply': bot_reply})#sends bot_reply to browser

#running app(local host:5000)
if __name__ == '__main__':
     app.run(host="0.0.0.0",port=int(environ.get("PORT", 5000)))
