import os
import json
import random

file_dir: str = "arquivos/usuarios.json"

LIMITES_RESERVA = (-23.5700, -23.5500, -46.6500, -46.6300)

def init_files() -> None:
    try:
        pasta: str = os.path.dirname(file_dir)
        if pasta and not os.path.exists(pasta):
            os.makedirs(pasta)
        
        if not os.path.exists(file_dir):
            with open(file_dir, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=4)
    except OSError as e:
        print(f"Erro de sistema ao inicializar arquivos: {e}")

def adicionar_usuario(login: str, senha: str) -> str:
    if not login or not senha:
        return "vazio"

    try:
        with open(file_dir, "r", encoding="utf-8") as file:
            usuarios: list[dict[str, str]] = json.load(file)

        for usuario in usuarios:
            if usuario["login"] == login:
                return "existe"

        novo_usuario: dict[str, str] = {"login": login, "senha": senha}
        usuarios.append(novo_usuario)

        with open(file_dir, "w", encoding="utf-8") as f:
            json.dump(usuarios, f, ensure_ascii=False, indent=4)

        return "sucesso"
    except (json.JSONDecodeError, IOError) as e:
        return f"erro_arquivo"

def remover_usuario(login: str) -> str:
    if not login:
        return "vazio"
        
    try:
        with open(file_dir, "r", encoding="utf-8") as file:
            usuarios: list[dict[str, str]] = json.load(file)
            
        usuario_encontrado = False
        for usuario in usuarios:
            if usuario["login"] == login:
                usuarios.remove(usuario)
                usuario_encontrado = True
                break
                
        if not usuario_encontrado:
            return "nao_encontrado"
            
        with open(file_dir, "w", encoding="utf-8") as f:
            json.dump(usuarios, f, ensure_ascii=False, indent=4)
            
        return "sucesso"
    except (json.JSONDecodeError, IOError):
        return "erro_arquivo"

def fazer_login(input_login: str, input_senha: str) -> bool:
    if not input_login or not input_senha:
        return False
        
    try:
        with open(file_dir, "r", encoding="utf-8") as file:
            usuarios: list[dict[str, str]] = json.load(file)

        for usuario in usuarios:
            if usuario["login"] == input_login and usuario["senha"] == input_senha:
                return True
        return False
    except (json.JSONDecodeError, IOError):
        return False

def obter_dados_telemetria() -> list[dict[str, any]]:
    esp1 = {
        "node_id": "ESP32-NODE-01",
        "alvo": "Onca-Pintada (Monitoramento 04)",
        "latitude": round(random.uniform(LIMITES_RESERVA[0], LIMITES_RESERVA[1]), 4),
        "longitude": round(random.uniform(LIMITES_RESERVA[2], LIMITES_RESERVA[3]), 4),
        "temperatura": round(random.uniform(37.5, 39.2), 1),
        "batimentos": random.randint(70, 110),
        "status": "Estavel"
    }

    esp2 = {
        "node_id": "ESP32-NODE-02",
        "alvo": "Lobo-Guara (Monitoramento 09)",
        "latitude": round(random.uniform(LIMITES_RESERVA[0], LIMITES_RESERVA[1]), 4),
        "longitude": round(random.uniform(LIMITES_RESERVA[2], LIMITES_RESERVA[3]), 4),
        "temperatura": round(random.uniform(38.0, 40.5), 1),
        "batimentos": random.randint(80, 135),
        "status": "Estavel"
    }

    if esp1["batimentos"] > 100 or esp1["temperatura"] > 39.0:
        esp1["status"] = "ALERTA: Alteracao Biometrica"
    
    if esp2["batimentos"] > 125 or esp2["temperatura"] > 40.0:
        esp2["status"] = "CRITICO: Possivel Estresse/Fuga"

    return [esp1, esp2]