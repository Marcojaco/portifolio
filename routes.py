from main import *
from flask import Flask, render_template, request, redirect, url_for



@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        if email == USUARIO_EMAIL and senha == USUARIO_SENHA:
            return redirect(url_for('home'))
        else:
            erro = 'Email ou senha incorreta!'
            return render_template('login.html', erro=erro)
        
    return render_template('login.html')


@app.route("/home")
def home():
    return render_template("home.html")
