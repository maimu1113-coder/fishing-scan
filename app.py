import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 診断パーツ
styles = ["悟りを開いた", "殺気ムンムンの", "魚にナメられた", "地球を釣る天才", "餌を寄付しに来た"]
jobs = ["サビキの貴公子", "根掛かりキング", "リリース担当大臣", "堤防の地蔵", "ルアー紛失職人"]
comments = ["魚を釣る前に自分を釣れ。", "エサの付け方が雑すぎるぞ。", "海を掃除して帰れ。", "魚が裏で笑っとるぞ。"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    score = random.randint(0, 100)
    res = f"【称号】：{random.choice(styles)}{random.choice(jobs)}\n【適正】：{score}%\n\n【一言】：{random.choice(comments)}"
    return jsonify({'result': res})
