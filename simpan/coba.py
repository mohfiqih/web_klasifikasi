# from flask import Flask, send_file, request, jsonify, render_template, redirect, url_for, session
# from flask_restx import Resource, Api, reqparse
# import pickle
# import numpy as np
# import pandas as pd
# import json
# from flask_mysqldb import MySQL

# app = Flask(__name__)
# api = Api(app, title='API Repo', default='API',
#           default_label='Repository Kuesioner')

# @app.route('/kuesioner')
# def ulasan():
#     return render_template('kuesioner.html')


# ulasan = "Hallo gess"
# print("Ini jawabannya : ", ulasan)

# import requests
# import json

# url = requests.get("https://localhost/web_skripsi/api/rest_jawaban/jawaban", verify=False)
# # print(url.status_code)
# data = url.text
# parse_json = json.loads(data)
# print(parse_json)

# @app.route('/testing')
# def ulasan():
#     return render_template('testing.html')

# import requests
# import json

# # @app.route('/testing/result', methods=['POST', 'GET'])
# def result():
#     if request.method == 'POST':
#         result = request.form['Data']
#         result_pred = model.predict(load_vec.transform([result]))
#         return render_template('testing.html', result=result_pred)

# result_pred
print("hallo")