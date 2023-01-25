from database import parserBodyKlasifikasi, LogKlasifikasi, db, parserParamKlasifikasi, app, db, api
from flask import Flask, send_file, request, jsonify, render_template, redirect, url_for, session
from flask_restx import Resource, Api, reqparse
import pickle
import numpy as np
import pandas as pd
import json

model = pickle.load(
    open('C:/xampp/htdocs/web_klasifikasi/model/model.pkl', 'rb'))
load_vec = pickle.load(
    open('C:/xampp/htdocs/web_klasifikasi/model/count_vect.pkl', 'rb'))


# @app.route('/testing')
# def ulasan():
#     return render_template('testing.html')


# @app.route('/testing/result', methods=['POST', 'GET'])
# def result():
#     if request.method == 'POST':
#         result = request.form['Data']
#         result_pred = model.predict(load_vec.transform([result]))
#         return render_template('testing.html', result=result_pred)

@app.route("/tabel", methods=["GET"])
def create_db():
    with app.app_context():
        db.create_all()
        return "Database Telah dibuat" + ' <a href="/"> Kembali</a>'


@api.route('/klasifikasi', methods=["GET", "POST"])
class KlasifikasiAPI(Resource):
    def get(self):
        log_data = db.session.execute(
            db.select(LogKlasifikasi.id, LogKlasifikasi.jawaban,
                      LogKlasifikasi.klasifikasi)).all()
        if (log_data is None):
            return f"Tidak Ada Data!"
        else:
            data = []
            for klas in log_data:
                data.append({
                    'id': klas.id,
                    'jawaban': klas.jawaban,
                    'klasifikasi': klas.klasifikasi,
                })
            return data

    @api.expect(parserBodyKlasifikasi)
    def post(self):
        # if request.method == "POST":
        args = parserBodyKlasifikasi.parse_args()
        jawaban = args["jawaban"]
        klasifikasi = model.predict(load_vec.transform([jawaban]))
        hasil = LogKlasifikasi(
                jawaban=jawaban,
                klasifikasi=klasifikasi,
        )
        db.session.add(hasil)
        db.session.commit()

        return jsonify({
            'Data Jawaban': jawaban,
            'Data Klasifikasi': klasifikasi,
            'message': f"Data jawaban berhasil masuk!"
        })


if __name__ == '__main__':
    app.run(debug=True)
