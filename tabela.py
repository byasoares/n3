from flask import Flask, render_template
import pymysql

app = Flask(__name__)


class Database:
    def __init__(self):
        host = "127.0.0.1"
        aluno = "aluno"
        sobrenome = "sobrenome"
        matricula = "matricula"
        database = "alunos"

        self.con = pymysql.connect(host=host, aluno=aluno, sobrenome=sobrenome, matricula=matricula, database=database, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()

    def lista_alunos(self):
        self.cur.execute("SELECT aluno, sobrenome, matricula FROM alunos LIMIT 50")
        result = self.cur.fetchall()

        return result

@app.route('/')
def alunos():

    def db_alunos():
        database = Database()
        matriculados = db.lista_alunos()

        return alunos


# tabela com dados recebidos