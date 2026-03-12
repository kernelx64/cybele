#!/bin/bash
clear
# 1. Verifica se a diretoria venv existe, se não, cria-a
if [ ! -d "venv" ]; then
    echo "[!] Creating virtual environment (venv)..."
    python -m venv venv
fi
# 2. Ativa o ambiente virtual
source venv/bin/activate

# 3. Executa a Cybele (o código trata das instalações das dependencias que precisa)
python src/cybele.py
deactivate