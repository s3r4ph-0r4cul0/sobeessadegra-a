import re
import os

def tratar(linhas, termo, diretorio, modulo="email_senha"):
    user_list = set()
    pass_list = set()

    for idx, linha in enumerate(linhas, 1):
        if termo not in linha:
            continue

        linha = linha.strip().replace('\r', '')
        if ':' not in linha:
            continue

        # Padrão: email:senha (2 partes)
        partes = linha.split(':')
        if len(partes) != 2:
            continue

        email, senha = partes
        email = email.strip()
        senha = senha.strip()

        # Valida email
        if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            user_list.add(email)

        # Valida senha
        if senha and len(senha) <= 16 and all(c.isprintable() for c in senha):
            pass_list.add(senha)

    if user_list:
        with open(os.path.join(diretorio, "user_list.txt"), "a", encoding="utf-8") as uf:
            uf.write('\n'.join(sorted(user_list)) + '\n')

    if pass_list:
        with open(os.path.join(diretorio, "pass_list.txt"), "a", encoding="utf-8") as pf:
            pf.write('\n'.join(sorted(pass_list)) + '\n')

if resultados:
    with open(os.path.join(diretorio, "result_search.txt"), "a", encoding="utf-8") as rf:
        rf.write('\n'.join(resultados) + '\n')
