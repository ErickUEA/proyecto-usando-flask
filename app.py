from flask import Flask
app = Flask(__name__)
def mensaje():
 @app.route('/')
 def home():
  return "<h1>¡Hola, Mundo</h1>"
 return app

@app.route('/usuario/<nombre>')
def usuario(nombre):
 return f"<h1>¡Hola, {nombre}!</h1>"

if __name__ == '__main__':
 app.mensaje()
 app.run()