import certifi
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.p2cn0.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=certifi.where())
db = client.spartagram

@app.route('/')
def home():
    return render_template('posting.html')

@app.route("/posting", methods=["GET"])
def posting_list_get():
    posting_num = list(db.posting.find({'num'}, {'_id': False}))
    return jsonify({'posting_list': posting_num})

@app.route('/user', methods=['POST'])
def posting_list_post():
    posting_list = list(db.posting.find({}, {'_id': False}))
    count = len(posting_list) + 1

    doc = {
        'num':count
    }
    db.posting.insert_one(doc)

@app.route('/posting', methods=['POST'])
def posting_post():
    url_receive = request.form['url_give']
    mylocation_receive = request.form['mylocation_give']
    mytime_receive = request.form['mytime_give']
    mytext_receive = request.form['mytext_give']

    posting_list = list(db.posting.find({}, {'_id': False}))
    count = len(posting_list) + 1

    doc = {
        'num':count,
        'url':url_receive,
        'mylocation':mylocation_receive,
        'mytime':mytime_receive,
        'mytext':mytext_receive
    }
    db.posting.insert_one(doc)

    return jsonify({'msg': '게시글 작성 완료'})

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)
