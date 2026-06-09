# OrbitBird Rescue System 🚀🦅

O **OrbitBird Rescue System** é um protótipo funcional de um terminal de operações e controle desenvolvido em Python. O sistema foca no monitoramento emergencial inteligente e na coordenação de equipes de busca e salvamento em áreas remotas, integrando conceitos de telemetria IoT (ESP32/MQTT) processados por fluxos no Node-RED e simulação de resgate em tempo real.

## 📋 Integrantes da Equipe (FIAP)

* **Artur Henrique Siqueira** – RM566986
* **Davi de Souza Malta** – RM560327
* **Guilherme Cruz Alves** – RM566861
* **Guilherme de Oliveira Scremin** – RM564788
* **Pedro Sales Ferreira** – RM566910

## 🛠️ Recursos e Funcionalidades Implementadas

O projeto foi construído utilizando **Python 3.10+** e aplica os conceitos fundamentais exigidos na grade de avaliação do Challenge:

* **Autenticação de Operadores:** Sistema de login e registro de novas contas para as Equipes de Busca terrestres.
* **Persistência em Arquivos:** Gravação e leitura segura de dados em formato JSON estruturado (`arquivos/usuarios.json`).
* **Tratamento de Exceções:** Uso de `try/except` para proteger operações de I/O e evitar corrupção de dados.
* **Painel de Telemetria IoT:** Simulação de pacotes de dados de nós sensores (ESP32) contendo geolocalização (GPS), temperatura e frequência cardíaca.
* **Simulador de Resgate:** Algoritmo para coordenação e cálculo de missões críticas nos modos "Localizar Alguém" e "Ser Localizado".

## 📁 Estrutura de Arquivos do Repositório

```text
├── main.py          # Arquivo principal (Fluxo do menu e loop interativo do terminal)
├── funcoes.py       # Módulo contendo as funções operacionais e lógicas de arquivos
└── arquivos/
	└── usuarios.json # Banco de dados local simulado (Gerado automaticamente)
```

## ▶️ Requisitos

* Python 3.10 ou superior

## ▶️ Como executar

1. Clone o repositório ou baixe os arquivos.
2. Navegue até a pasta do projeto e execute:

```bash
python main.py
```

Observação: o arquivo `arquivos/usuarios.json` é criado automaticamente ao registrar usuários.

---

Se quiser que eu adicione instruções de instalação específicas, um `requirements.txt` ou um exemplo de uso mais detalhado, diga e eu atualizo o `README.md`.

