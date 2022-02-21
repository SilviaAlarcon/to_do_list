from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

todos = ['TODO 1', 'TODO 2']

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    #Crea una cookie, parametros: nombre de la cookie y valor 
    response.set_cookie('user_ip', user_ip)

    return response


@app.route('/hello')
def hello():
    #Obtener una cookie almacenada
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip': user_ip,
        'todos': todos
    }
    return render_template('hello.html', **context)