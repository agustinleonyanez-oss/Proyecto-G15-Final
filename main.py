from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Bienvenido a Proyecto G15 Final</h1><p>Tu aplicación está funcionando correctamente.</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
