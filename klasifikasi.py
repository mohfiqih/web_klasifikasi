from flask import Flask, send_file, request, jsonify, render_template, redirect, url_for, session
from flask_restx import Resource, Api, reqparse
import pickle
import numpy as np
import pandas as pd
import json
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)
api = Api(app, title='API Repository', default='API',
          default_label='Repository Kuesioner')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'repository_skripsi'

mysql = MySQL(app)

# ARGS
parserParamJawaban = reqparse.RequestParser()
# parserParamJawaban.add_argument(
#     'id_respon', type=str, help='Masukan ID Respon', location='args')
parserParamJawaban.add_argument(
    'id_identitas', type=str, help='Masukan ID Identitas', location='args')
parserParamJawaban.add_argument(
    'nama_lengkap', type=str, help='Masukan Nama Lengkap', location='args')
parserParamJawaban.add_argument(
    'prodi', type=str, help='Masukan Prodi', location='args')
parserParamJawaban.add_argument(
    'sebagai', type=str, help='Sebagai', location='args')
parserParamJawaban.add_argument(
    'gender', type=str, help='Gender', location='args')
parserParamJawaban.add_argument(
    'pertanyaan', type=str, help='Pertanyaan', location='args')
parserParamJawaban.add_argument(
    'jawaban', type=str, help='Jawaban', location='args')

parserBodyJawaban = reqparse.RequestParser()
parserBodyJawaban.add_argument(
    'id_identitas', type=str, help='Masukan ID Identitas', location='args')
parserBodyJawaban.add_argument(
    'nama_lengkap', type=str, help='Masukan Nama Lengkap', location='args')
parserBodyJawaban.add_argument(
    'prodi', type=str, help='Masukan Prodi', location='args')
parserBodyJawaban.add_argument(
    'sebagai', type=str, help='Sebagai', location='args')
parserBodyJawaban.add_argument(
    'gender', type=str, help='Gender', location='args')
parserBodyJawaban.add_argument(
    'pertanyaan', type=str, help='Pertanyaan', location='args')
parserBodyJawaban.add_argument(
    'jawaban', type=str, help='Jawaban', location='args')

#

# Load Model
model = pickle.load(
    open('C:/xampp/htdocs/web_klasifikasi/model/model.pkl', 'rb'))
load_vec = pickle.load(
    open('C:/xampp/htdocs/web_klasifikasi/model/count_vect.pkl', 'rb'))


# Klasifikasi
@api.route('/klasifikasi', methods=["GET", "POST"])
class KlasifikasiAPI(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute(''' SELECT * FROM kuesioner ''')
        data = cur.fetchall()
        if (data is None):
            return f"Tidak Ada Data!"
        else:
            # return jsonify(data)
            wadah = []
            for row in data:
                wadah.append({
                    "ID": row[0],
                    # "ID Respon": row[1],
                    "ID Identitas": row[1],
                    "Nama Lengkap": row[2],
                    "Prodi": row[3],
                    "Sebagai": row[4],
                    "Gender": row[5],
                    "Pertanyaan": row[6],
                    "Jawaban": row[7],
                    "Hasil": row[8],
                    "Datecreated": row[9],
                })
            return jsonify(wadah)

    @api.expect(parserBodyJawaban)
    def post(self):
        if request.method == 'POST':
            args = parserBodyJawaban.parse_args()

            # order_by = cur.execute('''SELECT * FROM daftar_soal ORDER BY id_soal''', 'asc')
            # # id_soal = cur.execute(''' SELECT * FROM daftar_soal WHERE paket_id ''')
            # data = []
            # foreach(order_by as row){
            #     data.append(
            #         "ID": row[0],
            #         "ID Respon": row[1],
            #         "ID Identitas": row[2],
            #         "ID Paket": row[3],
            #         "ID Soal": row[4],
            #         "Jawaban": row[5],
            #         "Klasifikasi": row[6],
            #         "Tanggal": row[7],
            #     )
            # }
            # get = mysql.connection.cursor()

            # join = get.execute('''SELECT responden.id_respon, responden.id_identitas, responden.paket_id_responden, paket_soal.id_paket, daftar_soal.paket_id, daftar_soal.id_soal FROM responden, paket_soal, daftar_soal''')
            # # join_responden = get.execute('''SELECT paket_soal.id_paket, responden.paket_id_responden FROM paket_soal, responden''')
            # order_by = get.execute('''SELECT * FROM daftar_soal ORDER BY id_soal''')
            # group_by = get.execute('''SELECT * FROM daftar_soal GROUP BY id_soal ASC''')


            # id_respon = args["id_respon"]
            
            # id_paket_jawaban = args["id_paket_jawaban"]
            # id_soal_jawaban = args["id_soal_jawaban"]
            id_identitas = args["id_identitas"]
            nama_lengkap = args["nama_lengkap"]
            prodi = args["prodi"]
            sebagai = args["sebagai"]
            gender = args["gender"]
            pertanyaan = args["pertanyaan"]
            jawaban = args["jawaban"]
            klas = model.predict(load_vec.transform([jawaban]))
            hasil = np.array(klas)

            timestamp = 1674996979.12913
            date_time = datetime.fromtimestamp(timestamp)
            datecreated = date_time.strftime("%d-%m-%Y, %H:%M:%S")

            cur = mysql.connection.cursor()
            # cur.execute(''' INSERT INTO jawaban VALUES(%s,%s,%s,%s,%s,%s,%s,%s) ''', (id, id_respon,
            #             id_identitas, id_paket_jawaban, id_soal_jawaban, jawaban, klasifikasi, tanggal))
            # mysql.connection.commit()
            cur.execute(''' INSERT INTO kuesioner VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ''', (id,
                        id_identitas, nama_lengkap, prodi, sebagai, gender, pertanyaan, jawaban, hasil, datecreated))
            cur.close()

            return {
                'Identitas': id_identitas,
                'Nama Lengkap': nama_lengkap,
                'Prodi': prodi,
                'Sebagai': sebagai,
                'Gender': gender,
                'Pertanyaan': pertanyaan,
                'Jawaban': jawaban,
                'Hasil': hasil,
                'Datecreated': datecreated,
                'message': f"Data jawaban berhasil masuk!"
            }

            # return {
            #     'ID Responden': id_respon,
            #     'ID Identitas': id_identitas,
            #     'ID Paket': id_paket_jawaban,
            #     'ID Soal': id_soal_jawaban,
            #     'Jawaban': jawaban,
            #     'Klasifikasi': klasifikasi.tolist(),
            #     'Tanggal': tanggal,
            #     'message': f"Data jawaban berhasil masuk!"
            # }


# # ---------------- Test ------------------ #
# parserParamTest = reqparse.RequestParser()
# parserParamTest.add_argument(
#     'jawaban', type=str, help='Masukan Jawaban Anda', location='args')

# parserBodyTest = reqparse.RequestParser()
# parserBodyTest.add_argument(
#     'jawaban', type=str, help='Masukan Jawaban Anda', location='args')

# @api.route('/testing', methods=["GET", "POST"])
# class TestingNB(Resource):
#     @api.expect(parserBodyTest)
#     def post(self):
#         if request.method == 'POST':
#             args = parserBodyTest.parse_args()

#             jawaban = args["jawaban"]
#             klas = model.predict(load_vec.transform([jawaban]))
#             klasifikasi = np.array(klas)

#             timestamp = 1674996979.12913
#             date_time = datetime.fromtimestamp(timestamp)
#             tanggal = date_time.strftime("%d-%m-%Y, %H:%M:%S")

#             cur = mysql.connection.cursor()
#             cur.execute(''' INSERT INTO testing VALUES(%s,%s,%s,%s) ''', (id, jawaban, klasifikasi, tanggal))
#             mysql.connection.commit()
#             cur.close()

#             return {
#                 'Jawaban': jawaban,
#                 'Klasifikasi': klasifikasi.tolist(),
#                 'Tanggal': tanggal,
#                 'message': f"Data jawaban berhasil masuk!"
#             }


if __name__ == '__main__':
    app.run(debug=True, host="localhost")