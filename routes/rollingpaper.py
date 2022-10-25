from flask import Blueprint, render_template, request, jsonify
from db import db

rolling = Blueprint("rolling", __name__, template_folder="templates")


# 롤링 페이퍼 페이지 기본 정보 get
@rolling.route('/<url>')
def get_rollingpaper(url):
    print(url)

    # test 주석
    result = {'url': 'mina', 'rolling_id': 4, 'user_nickname': "mina", "cake_id": "choco"}
    message_count = db.message.count_documents({'rolling_id': 4})

    # result = db.rollingpaper.find_one({'url': url})
    # message_count = db.message.count_documents({'rolling_id': result['rolling_id']})

    print(result)
    print(message_count)

    # if(# 토큰 없을 경우 ):
    #     return render_template("guestMain.html", mainpage_info=result, message_count=message_count), 200
    #
    # else: # 토큰 있을 경우
    return render_template("rollingpaper.html", mainpage_info=result, message_conut=message_count), 200

# 롤링 페이지 캔들 정보 get
@rolling.route('/detail-data/<url>/<rolling_id>')
def get_candle(url, rolling_id):
    print(type(rolling_id))
    message_list = list(db.message.find({'rolling_id': int(rolling_id)}, {'_id': False}))
    print(message_list)
    return jsonify({'message_list': message_list}), 200
