import os
import threading
from concurrent.futures import ThreadPoolExecutor

from utils.banner import exibir_banner
from utils.arquivos import preparar_diretorio
from modulos import email_senha, url_email_senha, user_pass_block

DIRETORIO_FONTE = "/home/redteam01/Downloads/Telegram Desktop/file-apoio/"

contador_lock = threading.Lock()
arquivos_processados = 0

def mostrar_progresso(atual, total, largura=40):
    preenchido = int(largura * atual / total)
    vazio = largura - preenchido
    percentual = int(100 * atual / total)
    barra = '[' + '#' * preenchido + '-' * vazio + ']'
    print(f'\r{barra} {percentual:3d}% ({atual}/{total})', end='', flush=True)

def processar_arquivo(caminho_arquivo, termo, diretorio, total_arquivos):
    global arquivos_processados

    with open(caminho_arquivo, "r", encoding="utf-8", errors="ignore") as f:
        linhas = f.readlines()
    email_senha.tratar(linhas, termo, diretorio)
    url_email_senha.tratar(linhas, termo, diretorio)
    user_pass_block.tratar(linhas, termo, diretorio)

    with contador_lock:
        arquivos_processados += 1
        mostrar_progresso(arquivos_processados, total_arquivos)

def main():
    global arquivos_processados
    exibir_banner()
    termo = input("Informe o termo para busca: ").strip()
    if not termo:
        print("Erro: Nenhum termo informado.")
        return

    diretorio = preparar_diretorio(termo)

    arquivos = [f for f in os.listdir(DIRETORIO_FONTE) if f.endswith(".txt")]
    if not arquivos:
        print("Nenhum arquivo .txt encontrado no diretório:", DIRETORIO_FONTE)
        return

    total_arquivos = len(arquivos)
    arquivos_processados = 0

    with ThreadPoolExecutor(max_workers=4) as executor:
        for arquivo in arquivos:
            caminho_completo = os.path.join(DIRETORIO_FONTE, arquivo)
            executor.submit(processar_arquivo, caminho_completo, termo, diretorio, total_arquivos)

    print("\n✔️  Processamento concluído.")

if __name__ == "__main__":
    main()
