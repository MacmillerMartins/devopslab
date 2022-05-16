from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return "Desafio - Macmiller: Lab Cloud & DevOps"

if __name__ == '__main__':
    app.run()