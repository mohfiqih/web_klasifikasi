# from app import db, api, app
from flask import Flask, send_file, request, jsonify, render_template, redirect, url_for, session
from flask_restx import Resource, Api, reqparse

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app, title='API Repo', default='API',
          default_label='Repository Kuesioner')

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:''@localhost/repository_skripsi'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class LogKlasifikasi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jawaban = db.Column(db.String(2000), nullable=False)
    klasifikasi = db.Column(db.String(20), nullable=False)

    def __init__(self, jawaban, klasifikasi):
        self.jawaban = jawaban
        self.klasifikasi = klasifikasi

parserParamKlasifikasi = reqparse.RequestParser()
parserParamKlasifikasi.add_argument(
    'jawaban', type=str, help='Masukan Ulasan Anda', location='args')

parserBodyKlasifikasi = reqparse.RequestParser()
parserBodyKlasifikasi.add_argument(
    'jawaban', type=str, help='Masukan Ulasan Anda', location='args')
