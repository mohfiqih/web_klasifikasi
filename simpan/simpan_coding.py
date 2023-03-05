# import requests
# import json

# # response_API = requests.get('http://127.0.0.1:5000/klasifikasi')
# # print(response_API)
# # #print(response_API.status_code)

# url = requests.get("http://127.0.0.1:5000/klasifikasi", verify=False)
# print(url.status_code)
# data = url.text
# parse_json = json.loads(data)

# print(parse_json)

# @app.route('/testing')
# def ulasan():
#     return render_template('testing.html')


# @app.route('/testing/result', methods=['POST', 'GET'])
# def result():
#     if request.method == 'POST':
#         result = request.form['Data']
#         result_pred = model.predict(load_vec.transform([result]))
#         return render_template('testing.html', result=result_pred)



# @app.route("/tabel", methods=["GET"])
# def create_db():
#     with app.app_context():
#         db.create_all()
#         return "Database Telah dibuat" + ' <a href="/"> Kembali</a>'

# # from app import db, api, app
# from flask import Flask, send_file, request, jsonify, render_template, redirect, url_for, session
# from flask_restx import Resource, Api, reqparse

# # from flask_sqlalchemy import SQLAlchemy
# from flask_mysqldb import MySQL

# app = Flask(__name__)
# api = Api(app, title='API Repo', default='API',
#           default_label='Repository Kuesioner')

# # app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:''@localhost/repository_skripsi'
# # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# # db = SQLAlchemy(app)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'repository_skripsi'
 
# mysql = MySQL(app)

# cursor = mysql.connection.cursor()
 
# #Executing SQL Statements
# # cursor.execute(''' CREATE TABLE table_name(field1, field2...) ''')
# cursor.execute(''' INSERT INTO log_klasifikasi VALUES(jawaban,klasifikasi) ''')
# # cursor.execute(''' DELETE FROM table_name WHERE condition ''')
 
# #Saving the Actions performed on the DB
# mysql.connection.commit()
 
# #Closing the cursor
# cursor.close()

# # class LogKlasifikasi(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     jawaban = db.Column(db.String(2000), nullable=False)
# #     klasifikasi = db.Column(db.String(20), nullable=False)

# #     def __init__(self, jawaban, klasifikasi):
# #         self.jawaban = jawaban
# #         self.klasifikasi = klasifikasi

# parserParamAPI = reqparse.RequestParser()
# parserParamAPI.add_argument(
#     'jawaban', type=str, help='Masukan Ulasan Anda', location='args')

# parserBodyAPI = reqparse.RequestParser()
# parserBodyAPI.add_argument(
#     'jawaban', type=str, help='Masukan Ulasan Anda', location='args')

# # # Tabel Daftar Soal

# # class DaftarSoal(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     paket_id = db.Column(db.Integer, unique=True)
# #     soal = db.Column(db.Text, nullable=False)

# #     def __init__(self, paket_id, soal):
# #         self.paket_id = paket_id
# #         self.soal = soal

# # # Tabel Jawaban

# # class Jawaban(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     id_respon = db.Column(db.Integer, unique=True)
# #     id_identitas = db.Column(db.Integer, unique=True)
# #     id_paket_jawaban = db.Column(db.Integer, unique=True)
# #     id_soal_jawaban = db.Column(db.Integer, unique=True)
# #     # kategori_soal = db.Column(db.String(20), unique=True)
# #     jawaban = db.Column(db.Text, nullable=False)
# #     klasifikasi = db.Column(db.String(20), nullable=False)

# #     def __init__(self, id_respon, id_identitas, id_paket_jawaban, id_soal_jawaban,jawaban, klasifikasi):
# #         self.id_respon = id_respon
# #         self.id_identitas = id_identitas
# #         self.id_paket_jawaban = id_paket_jawaban
# #         self.id_soal_jawaban = id_soal_jawaban
# #         # self.kategori_soal = kategori_soal
# #         self.jawaban = jawaban
# #         self.klasifikasi = klasifikasi

# # parserParamJawaban = reqparse.RequestParser()
# # parserParamJawaban.add_argument(
# #     'id_respon', type=str, help='Masukan ID Respon', location='args')
# # parserParamJawaban.add_argument(
# #     'id_identitas', type=str, help='Masukan ID Identitas', location='args')
# # parserParamJawaban.add_argument(
# #     'id_paket_jawaban', type=str, help='Masukan ID Paket', location='args')
# # parserParamJawaban.add_argument(
# #     'id_soal_jawaban', type=str, help='Masukan ID Soal', location='args')
# # parserParamJawaban.add_argument(
# #     'jawaban', type=str, help='Masukan Jawaban Anda', location='args')

# # parserBodyJawaban = reqparse.RequestParser()
# # parserBodyJawaban.add_argument(
# #     'id_respon', type=str, help='Masukan ID Respon', location='args')
# # parserBodyJawaban.add_argument(
# #     'id_identitas', type=str, help='Masukan ID Identitas', location='args')
# # parserBodyJawaban.add_argument(
# #     'id_paket_jawaban', type=str, help='Masukan ID Paket', location='args')
# # parserBodyJawaban.add_argument(
# #     'id_soal_jawaban', type=str, help='Masukan ID Soal', location='args')
# # parserBodyJawaban.add_argument(
# #     'jawaban', type=str, help='Masukan Jawaban Anda', location='args')


# # Jawaban
# @api.route('/jawaban', methods=["GET", "POST"])
# class JawabanAPI(Resource):
#     def get(self):
#         cur = mysql.connection.cursor()
#         cur.execute(''' SELECT * FROM jawaban ''')
#         #fetching all records from database
#         data = cur.fetchall()
#         if (data is None):
#             return f"Tidak Ada Data!"
#         else:
#             return jsonify(data)

# # Paket Kuesioner
# @api.route('/paket_kuesioner', methods=["GET", "POST"])
# class PaketKuesioner(Resource):
#     def get(self):
#         cur = mysql.connection.cursor()
#         cur.execute(''' SELECT * FROM paket_soal ''')
#         #fetching all records from database
#         data = cur.fetchall()
#         if (data is None):
#             return f"Tidak Ada Data!"
#         else:
#             return jsonify(data)

# # Daftar Soal
# @api.route('/pertanyaan', methods=["GET", "POST"])
# class PertanyaanKuesioner(Resource):
#     def get(self):
#         cur = mysql.connection.cursor()
#         cur.execute(''' SELECT * FROM daftar_soal ''')
#         #fetching all records from database
#         data = cur.fetchall()
#         if (data is None):
#             return f"Tidak Ada Data!"
#         else:
#             return jsonify(data)

# ---------------------------------------- ----------------------------------------- #

# @app.route('/web_skripsi/kuesioner/identitas')
# def render_identitas():
#     return render_template('identitas.html')

# # Responden
# @app.route('/responden/<int:id_respon>', methods=['POST', 'GET'])
# def responden():
#     if request.method == 'POST':
#         # id_respon = request.form['id_respon']
#         id_identitas = request.form['id_identitas']
#         paket_id_responden = request.form['paket_id_responden']
#         nama_lengkap = request.form['nama_lengkap']
#         sebagai = request.form['sebagai']
#         gender = request.form['gender']

#         cur = mysql.connection.cursor()
#         cur.execute(''' INSERT INTO responden VALUES(%s,%s,%s,%s,%s,%s) ''',(id_respon,id_identitas,paket_id_responden,nama_lengkap,sebagai,gender))
#         mysql.connection.commit()
#         cur.close()

#         return redirect('/web_skripsi/kuesioner/pertanyaan/')
#     return render_template('kuesioner.html')

# @app.route('/web_skripsi/kuesioner/pertanyaan')
# def render_pertanyaan():
#     return render_template('pertanyaan.html')


# @app.route('/kuesioner/result', methods=['POST', 'GET'])
# def result():
#     if request.method == 'POST':
#         result = request.form['Data']
#         result_pred = model.predict(load_vec.transform([result]))
#         return render_template('kuesioner.html', result=result_pred)