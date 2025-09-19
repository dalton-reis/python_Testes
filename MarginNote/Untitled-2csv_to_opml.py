import subprocess
import os

# Verifica se o arquivo CSV existe
csv_file = "planilha_exemplo_mindmap.csv"
if not os.path.exists(csv_file):
    print(f"Erro: Arquivo {csv_file} não encontrado!")
    exit(1)

# Executa o comando csv2opml (assumindo que é o nome do programa)
try:
    subprocess.run([
        "csv2opml",  # Nome do programa converter
        csv_file, "planilha_exemplo_mindmap.opml",
        "--levels", "1", "2",
        "--note-cols", "3", "4",
        "--skip-header",
        "--collapse-empty-levels",
        "--root-title", "Exemplo de Mapa"
    ], check=True)
    print("Conversão concluída com sucesso!")
except FileNotFoundError:
    print("Erro: Programa 'csv2opml' não encontrado!")
    print("Você precisa instalar o conversor CSV para OPML primeiro.")
except subprocess.CalledProcessError as e:
    print(f"Erro durante a conversão: {e}")
except Exception as e:
    print(f"Erro inesperado: {e}")