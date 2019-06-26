import pymysql
from app import app
from lista_alunos import mysql
from flask import jsonify
from flask import flash, request



@app.route('/add', methods=['POST'])
def adicionar_aluno():
    try:
        _json = request.json
        _name = _json['nome']
        _sobrenome = _json['sobrenome']
        _matricula = _json['matricula']

        # confirmando os dados recebidos

        if _nome and _sobrenome and _matricula and request.method == 'POST':

            sql = "INSERT INTO tabela_usuario(user_nome, user_sobrenome, user_matricula) VALUES(%s, %s, %s)"
            data = (_nome, _sobrenome, _matricula,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Aluno Adicionado')
            resp.status_code = 200
            return resp
        else:
            return not_found()

        #inserindo dados na tabela
         # metodo post

    @app.route('/delete/')
    def deletar_aluno(id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tabela_usuario WHERE user_id=%s", (id,))
            conn.commit()
            resp = jsonify('Aluno deletado')
            resp.status_code = 200
            return resp

        # metodo delete