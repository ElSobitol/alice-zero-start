from flask import Flask, request
import logging
import json


app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)
@app.route("/", methods=["POST"])
def start():
    logging.info(request.json)
    response = {
        "version": request.json["version"],
        "session": request.json["session"],
        "response": {
            "end_session": False
        }
    }
    
    

    req = request.json
    if req["session"]["new"]:
        response["response"]["text"] = "Привет! Скажи, для какого случая тебе нужна цитата?"
        #Как только получили запрос - пишем ответ!
    else:
        if req["request"]["original_utterance"].capitalize() in ["Для важных переговоров"]:
            response["response"]["text"] = "Очевидно, да вы все ######, вот что очевидно!"
        elif req["request"]["original_utterance"].capitalize() in ["Цитаты великих"]:
            response["response"]["text"] = "Стремитесь не к успеху, а к ценностям, которые он дает"
#         elif req["request"]["original_utterance"].capitalize() in ["Спасибо"]:
#             response["response"]["text"] = "Всего доброго! Приходите ещё!"
            response["response"]["end_session"] = True
            
        
    return json.dumps(response)
