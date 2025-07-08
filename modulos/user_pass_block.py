import re
import os

def tratar(linhas, termo, diretorio, modulo="blocos_user_pass"):
    user_list = set()
    pass_list = set()
    encontrou_termo = False

    user = None
    passwd = None

    for linha in linhas:
        linha_strip = linha.strip()

        if termo.lower() not in linha_strip.lower():
            continue

        if re.match(r"^USER:", linha_strip, re.I):
            user = linha_strip.split(":", 1)[1].strip()
            if user:
                user_list.add(f"{user} (origem: {modulo})")
        elif re.match(r"^PASS:", linha_strip, re.I):
            passwd = linha_strip.split(":", 1)[1].strip()
            if passwd and len(passwd) <= 16 and all(c.isprintable() for c in passwd):
                pass_list.add(f"{passwd} (origem: {modulo})")

    if user_list:
        with open(os.path.join(diretorio, "user_list.txt"), "a", encoding="utf-8") as uf:
            uf.write('\n'.join(sorted(user_list)) + '\n')

    if pass_list:
        with open(os.path.join(diretorio, "pass_list.txt"), "a", encoding="utf-8") as pf:
            pf.write('\n'.join(sorted(pass_list)) + '\n')
