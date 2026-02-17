from flask import Flask, request, redirect, render_template, url_for
import os
import pandas as pd

app = Flask(__name__)

# Caminho absoluto do arquivo
basedir = os.path.abspath(os.path.dirname(__file__))
excel_file = os.path.join(basedir, "cadastro.xlsx")


@app.route("/")
def index():
    return redirect(url_for("registrar"))


@app.route("/registrar", methods=["GET", "POST"])
def registrar():

    if request.method == "POST":

        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")

        # Se arquivo existir, carrega
        if os.path.exists(excel_file):
            df = pd.read_excel(excel_file)
        else:
            df = pd.DataFrame(columns=["Nome", "Email", "Senha"])

        # Novo registro
        novo_registro = pd.DataFrame(
            [[nome, email, senha]],
            columns=["Nome", "Email", "Senha"]
        )

        # Adiciona ao DataFrame existente
        df = pd.concat([df, novo_registro], ignore_index=True)

        # Salva no Excel
        df.to_excel(excel_file, index=False, engine="openpyxl")

        return render_template("sucesso.html")

    return render_template("registrar.html")


if __name__ == "__main__":
    app.run(debug=True)
