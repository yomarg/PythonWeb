from flask import Flask, render_template # de la biblioteca de flack importaremos Flack

app = Flask(__name__) # inicializar con una variable name, y dicho valor se guardara en app

@app.route('/') # el @ funciona para crear un decorador, este comando en general, se utiliza para identificar la pagina principal
def homa():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html') # esta es la llamada de la Pagina 2

if __name__ == '__main__':
    app.run(debug=True)
