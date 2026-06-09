import os
import json
import random

file_dir: str = "arquivos/usuarios.json"

LIMITES_RESERVA = (-23.5700, -23.5500, -46.6500, -46.6300)

def init_files() -> None:
    """Inicializa o diretório e o arquivo de usuários.

    Cria a pasta (se necessário) e o arquivo JSON `usuarios.json` com
    uma lista vazia quando não existir. Em caso de erro de sistema
    imprime uma mensagem de erro.
    """
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
    """Adiciona um novo usuário ao arquivo JSON de usuários.

    Args:
        login: nome de usuário (string) a ser cadastrado.
        senha: senha associada ao usuário.

    Returns:
        'vazio' se `login` ou `senha` estiverem vazios;
        'existe' se o login já estiver cadastrado;
        'sucesso' em caso de gravação bem-sucedida;
        'erro_arquivo' em caso de erro de leitura/gravação do arquivo.
    """
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
    """Remove um usuário pelo `login` do arquivo JSON.

    Args:
        login: nome de usuário (string) a remover.

    Returns:
        'vazio' se `login` for vazio;
        'nao_encontrado' se o usuário não existir;
        'sucesso' em caso de remoção;
        'erro_arquivo' em caso de erro de leitura/gravação do arquivo.
    """
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
    """Verifica credenciais de login contra o arquivo de usuários.

    Args:
        input_login: nome de usuário a validar.
        input_senha: senha a validar.

    Returns:
        True se as credenciais corresponderem a um usuário cadastrado,
        False em caso contrário ou se ocorrer erro no arquivo.
    """
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
    """Gera dados de telemetria simulados para dois nós ESP32.

    Retorna uma lista de dicionários com campos como `node_id`,
    `alvo`, `latitude`, `longitude`, `temperatura`, `batimentos` e `status`.
    Os valores são gerados aleatoriamente dentro de limites predefinidos.
    """
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

def obter_simulacao_resgate_tempo_real(modo: str) -> list[str]:
    """Simula um fluxo textual de resgate em tempo real.

    Args:
        modo: 'localizar' para localizar outra pessoa, 'ser_localizado' para
              simular que você será localizado. Qualquer outro valor retorna
              uma lista com mensagem de opção inválida.

    Returns:
        Lista de strings contendo os passos/mensagens do simulador.
    """
    dispositivos: list[dict[str, any]] = obter_dados_telemetria()
    alvo: dict[str, any] = random.choice(dispositivos)
    missao: str = f"SR-{random.randint(1000, 9999)}"
    eta: int = random.randint(8, 24)

    if modo == "localizar":
        return [
            "--- SIMULADOR DE RESGATE EM TEMPO REAL ---",
            f"Missao {missao} recebida pelo centro de comando.",
            "Modo selecionado: localizar alguem.",
            f"Coordenadas recebidas: Lat {alvo['latitude']} | Long {alvo['longitude']}",
            f"Pessoa alvo: {alvo['alvo']}",
            "Sinal confirmado via satelite.",
            f"Espere que o resgate virá em aproximadamente {eta} minutos.",
        ]

    if modo == "ser_localizado":
        return [
            "--- SIMULADOR DE RESGATE EM TEMPO REAL ---",
            f"Missao {missao} recebida pelo centro de comando.",
            "Modo selecionado: ser localizado.",
            "Seu sinal de emergencia foi detectado.",
            f"Sua localizacao foi recebida em Lat {alvo['latitude']} | Long {alvo['longitude']}",
            f"Localizacao de {alvo['alvo']} encontrada nessas coordenadas.",
            "Resgate em deslocamento para o ponto informado.",
            f"Mantenha o sinal ativo. ETA estimado: {eta} minutos.",
        ]

    return [
        "--- SIMULADOR DE RESGATE EM TEMPO REAL ---",
        "Opcao invalida no simulador.",
        "Selecione localizar alguem ou ser localizado.",
    ]