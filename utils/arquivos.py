import os

def preparar_diretorio(termo: str) -> str:
    diretorio = os.path.join(os.getcwd(), termo.replace(" ", "_"))
    if not os.path.isdir(diretorio):
        os.makedirs(diretorio)
    # Garante arquivos base
    for arquivo in ["user_list.txt", "pass_list.txt", "result_search.txt", "Desconhecido.txt"]:
        path = os.path.join(diretorio, arquivo)
        if not os.path.isfile(path):
            with open(path, "w", encoding="utf-8") as f:
                pass
    return diretorio
