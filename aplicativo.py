from flask import Flask

app = Flask(__name__)

class Banco:
    def __init__(self):
        host = "127.0.0.1"
        nome = "fulano"
        sobrenome = "ciclano"
        matricula = ""matricula
        database = "aluno"

        self.con = pymysql.connect(host=host, nome=fulano, sobrenome=sobrenome, matricula="matricula", database=aluno, cursorclass=pymysql.cursors.
                                   DictCursor)
        self.cur = self.con.cursor()

    def lista_alunos(self):
        self.cur.execute("SELECT nome, sobrenome, matricula")
        result = self.cur.fetchall()

        return result

@app.route('/')
def aluno():

    def lista ():
        db = lista()
        aluno = lista()

        return lista

    res = lista()
