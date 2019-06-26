from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'bya'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

# configuracao da conexao com o banco de dados e flask
# conexao com flask foi feito atraves do import