import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request


@app.route('/add', methods=['POST'])
def adicionar_aluno():
    try:
        _json = request.json
        _nome = _json['nome']
        _sobrenome = _json['sobrenome']
        _matricula = _json['matricula']


        if _nome and _sobrenome and _matricula and request.method == 'POST':

            sql = "INSERT INTO tbl_user(user_name, user_email, user_password) VALUES(%s, %s, %s)"

            #inserindo os dados na tabela

            data = (_nome, _sobrenome, _matricula,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Aluno cadastrado')
            resp.status_code = 200
            return resp

    # validar/salvar os valores

    @app.route('/delete/')
    def deletar_aluno():
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tbl_user WHERE user_id=%s", (id,))
            conn.commit()
            resp = jsonify('User deleted successfully!')
            resp.status_code = 200
            return resp