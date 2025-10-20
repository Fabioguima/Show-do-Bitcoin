# ₿ Show do Bitcoin

Um jogo interativo de perguntas e respostas inspirado em _“Show do Milhão”_, onde o jogador acumula prêmios em **Bitcoin (BTC)** ao acertar perguntas de diferentes níveis de dificuldade.  
O objetivo é responder corretamente todas as perguntas e alcançar o prêmio máximo!

---

## 🧩 Funcionalidades

- Perguntas divididas em três níveis: **Easy**, **Medium** e **Hard**
- Sistema de **pulos** (3 disponíveis por jogo)
- Opção de **desistência** com 50% do prêmio acumulado
- Em caso de erro, o jogador recebe 10% do valor conquistado
- Download automático de novas perguntas usando a **API Tryvia**
- Interface de terminal colorida com **Colorama**

---

## 🧠 Níveis e Regras

Dificuldade Nº de Perguntas Recompensa por Acerto Observações
🟢 Fácil 3 perguntas +0.1 BTC cada Início do jogo
🟡 Médio 3 perguntas +0.1 BTC cada Aumenta a tensão
🔴 Difícil 4 perguntas +0.1 BTC cada Final decisivo!

📉 Errou → Ganha 10% do valor acumulado
💸 Desistiu → Ganha 50% do valor acumulado
🏆 Acertou todas → 1.0 BTC total!

---

## 🏗️ Estrutura do Projeto

```
Show_do_bitcoin/
├── perguntas_bitcoin/
│   ├── perguntas_easy.json
│   ├── perguntas_medium.json
│   ├── perguntas_hard.json
│   ├── ran_perguntas.py
│   ├── download_perg.py
│   └── ...
├── contador_nivel.py
├── resposta_user.py
├── show_bitcoin.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Instalação e Execução

### 1. Clone o repositório

```bash
git clone https://github.com/Fabioguima/Show-do-Bitcoin.git
cd show-do-bitcoin
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o jogo

```bash
python show_bitcoin.py
```

---

## 📚 Dependências

Listadas em `requirements.txt`:

```
colorama==0.4.6
requests==2.32.3
```

---

## 🎮 Como Jogar

1. O jogo exibe perguntas de múltipla escolha (1 a 4).
2. Você pode:
   - Digitar o número da resposta correta
   - Digitar **P** para pular a pergunta (máx. 3 pulos)
   - Digitar **D** para desistir (ganha 50% do prêmio acumulado)
3. Se errar, o jogo termina e você ganha 10% do valor conquistado.
4. Responda todas as perguntas corretamente e ganhe o prêmio máximo em BTC!

---

## 🌐 Fonte das Perguntas

As perguntas são baixadas da API pública:

```
https://tryvia.ptr.red/api.php
```

O arquivo `download_perg.py` gerencia o download e o salvamento das perguntas em JSON.

---

## 👨‍💻 Autor

**Fábio Guimarães**  
📧 fguimaraesmielczarski@gmail.com  
💼 *https://github.com/Fabioguima*

---

## 🪪 Licença

Este projeto está licenciado sob a licença **MIT** — veja o arquivo [LICENSE](LICENSE) para mais detalhes.
