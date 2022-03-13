from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
io = SocketIO(app)

@app.route("/")
def main():
    message = "Olá, USUÁRIO. Está pronto para mais uma partida hoje?"
    return render_template("index.html", message=message)


@io.on('login')
def login_handler(data):
    print('def login ==> ', data)
    print(f'Usuário {data["id"]} conectado com sucesso!')

if __name__ == "__main__":
    io.run(app, debug=True)    