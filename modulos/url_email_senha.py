import re
import os

def tratar(linhas, termo, diretorio, modulo="url_email_senha"):
    user_list = set()
    pass_list = set()
    resultados = []  # <== acumula linhas com o termo

    for idx, linha in enumerate(linhas, 1):
        if termo not in linha:
            continue

        linha = linha.strip().replace('\r', '')
        partes = linha.split(':')
        if len(partes) != 3:
            continue

        url, email, senha = partes
        email = email.strip()
        senha = senha.strip()

        if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            user_list.add(email)

        if senha and len(senha) <= 16 and all(c.isprintable() for c in senha):
            pass_list.add(senha)

        resultados.append(f"{idx}:{linha}")  # salva linha com índice

    if user_list:
        with open(os.path.join(diretorio, "user_list.txt"), "a", encoding="utf-8") as uf:
            uf.write('\n'.join(sorted(user_list)) + '\n')

    if pass_list:
        with open(os.path.join(diretorio, "pass_list.txt"), "a", encoding="utf-8") as pf:
            pf.write('\n'.join(sorted(pass_list)) + '\n')

    if resultados:
        with open(os.path.join(diretorio, "result_search.txt"), "a", encoding="utf-8") as rf:
            rf.write('\n'.join(resultados) + '\n')
