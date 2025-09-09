from flask import Flask, render_template, request, redirect, url_for
import json, smtplib, ssl
from email.message import EmailMessage
import os

app = Flask(__name__)
ARQUIVO = "destinatarios.json"

def carregar_destinatarios():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return []

def salvar_destinatarios(lista):
    with open(ARQUIVO, "w") as f:
        json.dump(lista, f, indent=4)

def enviar_email(assunto, corpo):
    remetente = "seuemail@gmail.com"
    senha = "sua_senha_ou_senha_de_app"
    destinatarios = carregar_destinatarios()

    if not destinatarios:
        return

    msg = EmailMessage()
    msg["From"] = remetente
    msg["To"] = ", ".join(destinatarios)
    msg["Subject"] = assunto
    msg.set_content(corpo)

    contexto = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=contexto) as smtp:
        smtp.login(remetente, senha)
        smtp.send_message(msg)

@app.route("/", methods=["GET", "POST"])
def index():
    mensagem = ""
    lista = carregar_destinatarios()

    if request.method == "POST":
        if "email" in request.form:
            email = request.form["email"].strip()
            if email and email not in lista:
                lista.append(email)
                salvar_destinatarios(lista)
                mensagem = "Destinatário adicionado!"
            else:
                mensagem = "E-mail inválido ou já cadastrado."

        elif "nivel" in request.form:
            nivel = request.form["nivel"]
            if nivel == "baixo":
                assunto = "Alerta de Incêndio: Nível Baixo"
                corpo = "⚠️ Pequeno foco de incêndio. Tome cuidado!"
            elif nivel == "alto":
                assunto = "🚨 Alerta de Incêndio: Nível Alto"
                corpo = "🚨 Incêndio grave! Evacue imediatamente!"
            else:
                assunto = corpo = ""
            if assunto:
                enviar_email(assunto, corpo)
                mensagem = f"Alerta '{nivel}' enviado!"

        elif "remover" in request.form:
            email = request.form["remover"]
            if email in lista:
                lista.remove(email)
                salvar_destinatarios(lista)
                mensagem = f"{email} removido."

    return render_template("index.html", destinatarios=lista, mensagem=mensagem)

if __name__ == "__main__":
    app.run(debug=True)
