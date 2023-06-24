from flask import Flask, send_file, request, jsonify, render_template, redirect, url_for, session
from flask_restx import Resource, Api, reqparse
import pickle
import numpy as np
import pandas as pd
import json
from flask_mysqldb import MySQL
from datetime import datetime
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app, title='API Repository', default='API',
          default_label='Repository Kuesioner')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'repository_skripsi'

mysql = MySQL(app)

# app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@127.0.0.1:3306/repository_skripsi'
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["SQLALCHEMY_ECHO"] = True

# db = SQLAlchemy(app)
# CORS(app)

# Load Model
model = pickle.load(
    open('C:/xampp/htdocs/web_klasifikasi/model/model.pkl', 'rb'))
load_vec = pickle.load(
    open('C:/xampp/htdocs/web_klasifikasi/model/count_vect.pkl', 'rb'))

parserParamTest = reqparse.RequestParser()
parserParamTest.add_argument(
    'jawaban', type=str, help='Masukan Jawaban Anda', required=True)

parserBodyTest = reqparse.RequestParser()
parserBodyTest.add_argument(
    'jawaban', type=str, help='Masukan Jawaban Anda', required=True)


# class Klasifikasi(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     id_identitas = db.Column(db.String(500), nullable=False)
#     nama_lengkap = db.Column(db.String(500), nullable=False)
#     prodi = db.Column(db.String(500), nullable=False)
#     sebagai = db.Column(db.String(500), nullable=False)
#     gender = db.Column(db.String(500), nullable=False)
#     id_paket_jawaban = db.Column(db.String(500), nullable=False)
#     jawaban = db.Column(db.String(500), nullable=False)
#     label = db.Column(db.String(500), nullable=False)

#     def __init__(self, id_identitas, nama_lengkap, prodi, sebagai, gender, id_paket_jawaban, jawaban, label):
#         self.id_identitas = id_identitas
#         self.nama_lengkap = nama_lengkap
#         self.prodi = prodi
#         self.sebagai = sebagai
#         self.gender = gender
#         self.id_paket_jawaban = id_paket_jawaban
#         self.jawaban = jawaban
#         self.label = label


# @api.route('/testApi', methods=['POST'])
# class TestAPI(Resource):
#     # @api.expect(parserBodyTest)
#     def post(self):
#         # if request.method == 'POST':
#             # args = parserBodyTest.parse_args()
#             id_identitas = request.form['id_identitas']
#             nama_lengkap = request.form['nama_lengkap']
#             prodi = request.form['prodi']
#             sebagai = request.form['sebagai']
#             gender = request.form['gender']
            
#             id_paket_jawaban = request.form['id_paket_jawaban']
#             jawaban = request.form['jawaban']
#             klas = model.predict(load_vec.transform([jawaban]))
#             # label = np.array(klas[0])

#             test = Klasifikasi(
#                 id_identitas=id_identitas,
#                 nama_lengkap=nama_lengkap,
#                 prodi=prodi,
#                 sebagai=sebagai,
#                 gender=gender,
#                 id_paket_jawaban=id_paket_jawaban,
#                 jawaban=jawaban,
#                 label=klas
#             )
#             db.session.add(test)
#             db.session.commit()

#             return json.dumps({
#                 'id_identitas': id_identitas,
#                 'nama_lengkap': nama_lengkap,
#                 'prodi': prodi,
#                 'sebagai': sebagai,
#                 'gender': gender,
#                 'id_paket_jawaban': id_paket_jawaban,
#                 'jawaban': jawaban,
#                 'label': label.tolist(),
#                 'message': f"Data jawaban berhasil masuk!"
#             })

    # def get(self):
    #     log_data = db.session.execute(
    #         db.select(Klasifikasi.id, Klasifikasi.jawaban, Klasifikasi.klasifikasi)).all()
    #     if (log_data is None):
    #         return f"Tidak Ada Data Tilang!"
    #     else:
    #         data = []
    #         for history in log_data:
    #             data.append({
    #                 'id': history.id,
    #                 'jawaban': history.jawaban,
    #                 'klasifikasi': history.klasifikasi,
    #             })
    #         return data

@app.route('/postData', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        id_identitas = request.form['id_identitas']
        nama_lengkap = request.form['nama_lengkap']
        prodi = request.form['prodi']
        sebagai = request.form['sebagai']
        gender = request.form['gender']
        id_paket_jawaban = request.form['id_paket_jawaban']
        jawaban = request.form['jawaban']
            
        klas = model.predict(load_vec.transform([jawaban]))
        label = np.array(klas[0])
            
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO klasifikasi VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s) ''', (id, id_identitas, nama_lengkap, prodi, sebagai, gender, id_paket_jawaban, jawaban, label.tolist()))
        mysql.connection.commit()

        return {
                'Identitas': id_identitas,
                'Nama Lengkap': nama_lengkap,
                'Prodi': prodi,
                'Sebagai': sebagai,
                'Gender': gender,
                'id_paket_jawaban': id_paket_jawaban,
                'Jawaban': jawaban,
                'label': label.tolist(),
                'message': f"Data jawaban berhasil masuk!"
        }
        
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute(''' SELECT * FROM klasifikasi ''')
        data = cur.fetchall()
        if (data is None):
                return f"Tidak Ada Data!"
        else:
            wadah = []
            for row in data:
                wadah.append({
                        "ID": row[0],
                        "ID Identitas": row[1],
                        "Nama Lengkap": row[2],
                        "Prodi": row[3],
                        "Sebagai": row[4],
                        "Gender": row[5],
                        "Id Paket": row[6],
                        "Jawaban": row[7],
                        "Label": row[8],
                    })
            return wadah
            
    # return "Hallo, Route Utama! API Siap Pakai!"

# @app.route('/getData')
# def getData():
#         cur = mysql.connection.cursor()
#         cur.execute(''' SELECT * FROM klasifikasi ''')
#         data = cur.fetchall()

#         if (data is None):
#             return f"Tidak Ada Data!"
#         else:
#             wadah = []
#             for row in data:
#                 wadah.append({
#                     "ID": row[0],
#                     "ID Identitas": row[1],
#                     "Nama Lengkap": row[2],
#                     "Prodi": row[3],
#                     "Sebagai": row[4],
#                     "Gender": row[5],
#                     "Pertanyaan": row[6],
#                     "Jawaban": row[7],
#                     "Hasil": row[8],
#                     "Datecreated": row[9],
#                 })
#             return wadah

# @app.route('/send', methods=['GET', 'POST'])
# def send():
#     if request.method == 'POST':
#         id_identitas = request.form['id_identitas']
#         nama_lengkap = request.form['nama_lengkap']
#         prodi = request.form['prodi']
#         sebagai = request.form['sebagai']
#         gender = request.form['gender']
#         id_paket_jawaban = request.form['id_paket_jawaban']
#         jawaban = request.form['jawaban']
#         label = request.form['label']

#         cursor = mysql.connection.cursor()
#         cursor.execute(''' INSERT INTO klasifikasi VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s) ''', (id, id_identitas, nama_lengkap, prodi, sebagai, gender, id_paket_jawaban, jawaban, label))
#         mysql.connection.commit()
        
#         return 'Berhasil Kirim Data!'

#     return "Hallo, Route Utama! API Siap Pakai!"
#         # if not user:
        #     return f'Email {email} tidak Ada!', 400
        # else:
        #     user = user[0]

        # if email:
        #     return {
        #         'email': user.email,
        #         'nama': user.name,
        #         # 'tanggal': user.created_at
        #     }

if __name__ == '__main__':
    # app.run(debug=True, ssl_context='adhoc')
    app.run(debug=True)
