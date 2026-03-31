# Tic Tac Toe com IA (Minimax) em Python 🤖

Este projeto é uma implementação do clássico **Jogo da Velha (Tic Tac Toe)** utilizando **Inteligência Artificial** com o algoritmo **Minimax**.

A IA analisa todas as jogadas possíveis antes de decidir onde jogar, garantindo sempre a melhor escolha.  
Se o algoritmo for executado corretamente, a IA **nunca perde**, podendo apenas empatar.

O jogo funciona diretamente no **terminal** e permite que o usuário jogue contra o computador.

---

## 📌 Funcionalidades

- Jogador vs Inteligência Artificial
- IA utiliza algoritmo **Minimax**
- Usuário escolhe o símbolo (X ou O)
- Sorteio automático de quem começa
- Verificação automática de vitória
- Verificação de empate
- Interface simples no terminal
- Validação de jogadas inválidas
- IA toma decisões ótimas

---

## 🧠 Algoritmo utilizado

O projeto utiliza o algoritmo **Minimax**, muito usado em jogos de estratégia para encontrar a melhor jogada possível considerando todos os cenários futuros.

O algoritmo funciona simulando todas as possibilidades de jogadas até o final da partida.

A IA sempre busca:

- Maximizar suas chances de vitória
- Minimizar as chances do jogador vencer

Pontuação utilizada pelo algoritmo:

- **+10** → IA vence
- **-10** → Jogador vence
- **0** → Empate

---

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/tic-tac-toe-minimax-python.git
```

### 3. Execute o programa

---

## 🎮 Como jogar

O tabuleiro possui posições numeradas de **0 a 8**:

```
 0 | 1 | 2
-----------
 3 | 4 | 5
-----------
 6 | 7 | 8
```

Escolha um número correspondente à posição onde deseja jogar.

Exemplo:

```
Escolha uma posição (0-8): 4
```

---

## 🛠 Tecnologias utilizadas

* Python 3
* Algoritmo Minimax
* Biblioteca math
* Biblioteca random

---

## 📚 Estrutura do projeto

```
tic-tac-toe-minimax-python
│
├── README.md
├── Tic Tac Toe Documentation.pdf
└── main.py
```

## 👨‍💻 Autores

Projeto desenvolvido por:

* Arthur Azevedo Locce Baptista
* Ryan Chaves Dias
* Sophia Franco de Godoy

---

Projeto criado para estudo de **Inteligência Artificial**, **Algoritmo Minimax** e **lógica de programação em Python**.
