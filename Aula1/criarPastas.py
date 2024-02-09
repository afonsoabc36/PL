import os

# Mudar diretoria
os.chdir('./PL2024')

# Criar pastas TPC
for i in range(8):
    nomePasta = f"TP{i+1}"

    os.mkdir(nomePasta)

    open(f"{nomePasta}/.gitkeep", "w")