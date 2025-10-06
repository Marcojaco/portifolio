from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = "trojan"  


USUARIO_EMAIL = "marcoborges249@gmail.com"
USUARIO_SENHA = "marcofilho09"

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        if email == USUARIO_EMAIL and senha == USUARIO_SENHA:
            session['logado'] = True  
            return redirect(url_for('home'))
        else:
            erro = "Email ou senha incorretos!"
            return render_template('login.html', erro=erro)

    return render_template('login.html')

@app.route('/home')
def home():
    if not session.get('logado'): 
        return redirect(url_for('login'))
    return render_template('home.html')

@app.route('/logout')
def logout():
    session.pop('logado', None)  
    return redirect(url_for('login'))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host="0.0.0.0", port=port, debug=True)
