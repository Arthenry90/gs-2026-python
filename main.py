import os
from funcoes import init_files, adicionar_usuario, fazer_login, obter_dados_telemetria, obter_simulacao_resgate_tempo_real

def limpar_tela() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho() -> None:
    limpar_tela()
    print("=" * 60)
    print(" SPACE RESCUE SYSTEM - Terminal de Operacoes")
    print(" Monitoramento Emergencial Inteligente em Areas Remotas")
    print("=" * 60)

init_files()

while True:
    exibir_cabecalho()
    print("\nSeja bem-vindo(a) ao sistema de comando e controle!")
    print("Por favor, selecione a opcao desejada:\n")
    
    print("[ 1 ] Fazer login de Operador")
    print("[ 2 ] Registrar nova conta da Equipe de Busca")
    print("[ 3 ] Painel de Telemetria (Sensores ESP32 / MQTT)")
    print("[ 4 ] Iniciar Simulador de Resgate em Tempo Real")
    print("[ 5 ] Sobre o Projeto (Missao, Visao e ODS)")
    print("[ 0 ] Desconectar e Sair")
    
    opcao: str = input("\nDigite o numero da opcao: ")
    
    match opcao:
        case "1":
            limpar_tela()
            print("--- LOGIN DE OPERADOR ---")
            input_login: str = input("Digite o seu login: ").strip()
            input_senha: str = input("Digite a sua senha: ").strip()
            
            print(f"\nAutenticando usuario '{input_login}' via conexao segura...")
            
            if fazer_login(input_login, input_senha):
                print("\nConexao efetuada com sucesso! Acesso liberado.")
            else:
                print("\nAVISO: Login ou senha nao encontrados ou invalidos!")
                
            input("\nPressione ENTER para voltar ao menu...")
            
        case "2":
            limpar_tela()
            print("--- REGISTRO DE NOVA CONTA ---")
            login: str = input("Digite o novo login: ").strip()
            senha: str = input("Digite a nova senha: ").strip()

            resultado: str = adicionar_usuario(login, senha)

            match resultado:
                case "vazio":
                    print("\nAVISO: Login e senha nao podem estar vazios!")
                    input("\nPressione ENTER para continuar...")
                case "existe":
                    print("\nAVISO: Este login ja esta cadastrado!")
                    input("\nPressione ENTER para voltar...")
                case "sucesso":
                    print("\nSucesso: Usuario registrado com sucesso!")
                    input("\nPressione ENTER para voltar ao menu...")
            
        case "3":
            limpar_tela()
            print("--- PAINEL DE TELEMETRIA IoT (FIWARE / MQTT) ---")
            print("Conectando ao Broker... Recebendo pacotes de dados via Satelite...\n")

            dispositivos: list[dict[str, any]] = obter_dados_telemetria()

            for esp in dispositivos:
                print("-" * 50)
                print(f"ID do Dispositivo: {esp['node_id']}")
                print(f"Alvo Atrelado:     {esp['alvo']}")
                print(f"Localizacao GPS:  Lat {esp['latitude']} | Long {esp['longitude']}")
                print(f"Temperatura Corp: {esp['temperatura']}C")
                print(f"Frequencia Card:  {esp['batimentos']} BPM")
                print(f"Status do No:      {esp['status']}")
            
            print("-" * 50)
            input("\nPressione ENTER para atualizar e voltar ao menu...")

        case "4":
            while True:
                limpar_tela()
                print("--- SIMULADOR DE RESGATE EM TEMPO REAL ---")
                print("Escolha o modo de operacao:\n")
                print("[ 1 ] Localizar alguem")
                print("[ 2 ] Ser localizado")
                print("[ 0 ] Voltar ao menu principal")

                opcao_resgate: str = input("\nDigite o numero da opcao: ").strip()

                match opcao_resgate:
                    case "1":
                        limpar_tela()
                        for linha in obter_simulacao_resgate_tempo_real("localizar"):
                            print(linha)
                        input("\nPressione ENTER para continuar...")
                        break
                    case "2":
                        limpar_tela()
                        for linha in obter_simulacao_resgate_tempo_real("ser_localizado"):
                            print(linha)
                        input("\nPressione ENTER para continuar...")
                        break
                    case "0":
                        break
                    case _:
                        print("\nAVISO: Opcao invalida no simulador!")
                        input("\nPressione ENTER para continuar...")
            
        case "5":
            limpar_tela()
            print("--- SOBRE O SPACE RESCUE SYSTEM ---")
            print("O Space Rescue System consiste em uma plataforma inteligente")
            print("de monitoramento emergencial desenvolvida para auxiliar operacoes")
            print("de localização e resgate em areas remotas (Montanhas e Florestas).")
            print("\nTecnologia baseada em Edge Computing (ESP32), MQTT e Satelite.")
            print("Alinhado com os Objetivos de Desenvolvimento Sustentavel (ODS) da ONU.")
            input("\nPressione ENTER para voltar ao menu...")

        case "0":
            limpar_tela()
            print("Encerrando conexao com a rede...")
            print("Sistema encerrado com sucesso. Ate logo!")
            break
            
        case _:
            print("\nAVISO: Opcao invalida! Por favor, escolha um numero do menu.")
            input("\nPressione ENTER para continuar...")