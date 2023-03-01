# Um Curso de Programação em Python

Esse curso foi feito para ajudar uns amigos a entrarem nesse mundo de tecnologia e também como uma forma de armazenar meu conhecimento na area.

Se você estiver curioso para saber os conteudos, dê uma olhada no [Índice](./Indice.md)

**Todos os códigos (que não são de lives nem de tutelagens de mal-código) nesse repositório são escritos seguindo o [PyLint](https://github.com/PyCQA/pylint), passam por um pre-commit e são formatados usando o [black](https://github.com/psf/black)**

## Links Uteis

- [Python Subreddit](https://www.reddit.com/r/Python/)
- [LearnPython Subreddit](https://www.reddit.com/r/learnpython)
- [PythonTips Subreddit](https://www.reddit.com/r/pythontips)
- [Python Discord](https://www.pythondiscord.com)
- [Site Oficial do Python](https://www.python.org)
- [CodeTriage](https://www.codetriage.com) (Contribua para projetos Open-Source)

Para quem preferir, também existem os vídeos do Gustavo Guanabara sobre Python.
- [Mundo 1](https://www.cursoemvideo.com/curso/python-3-mundo-1/)
- [Mundo 2](https://www.cursoemvideo.com/curso/python-3-mundo-2/)
- [Mundo 3](https://www.cursoemvideo.com/curso/python-3-mundo-3/)

## Milestones (Projetos)

Até o presente momento, você construirá 11 projetos (pode variar no futuro):

- Milestone 1: Criar uma Biblioteca de Filmes
- Milestone 2: Criando Biblioteca de Livros
- Milestone 3: Um Scraper de Citações
- Milestone 4: Um Scraper de Livros
- Milestone 5: Um Bot para o Discord
- Milestone 6: Um Editor de Texto
- Milestone 7: Um App de Pintura
- Milestone 8: Um Perceptron
- Milestone 9: Uma TCP Chat Room
- Milestone 10: TCP Chat Room Criptografada
- Milestone 11: Cliente Torrent

## Notas

Uma explicação de cada pasta:
- A pasta [Classes](./Classes/ReadMe.md) contém a versão escrita do que será ensinado/dito nas lives
- A pasta [Code](./Code/ReadMe.md) contém o codigo escrito durante as aulas
- A pasta [Exercicios](./Exercicios/ReadMe.md) contém praticas e pequenos desafios passados
- A pasta [Milestones](./Exercicios/Milestones/ReadMe.md) contém os grandes projetos/milestones

### Como Instalar o Python

A instalação do Python depende do seu OS, começarei explicando o processo no Windows e partirei para o Linux.

#### Instalando o Python no Windows

Aqui a instalação é "dividida" em duas partes, o interpretador e o executável no CMD/PATH.

Para instalar o interpretador, acesse a página de download clicando [aqui](https://www.python.org/downloads/windows/), escolha a versão estável mais recente (ou uma superior ou igual a 3.10), e baixe o instalador para sua versão do windows (32 ou 64 bits).

A instalação é bem tranquila, basta seguir com as opções padrões.

Para instalar o executável no CMD acesse a Microsoft Store e baixe o executável compativel com a versão escolhida pro interpretador.

O ambiente virtual é uma espécie de container para o seu código, separando cada projeto do seu sistema, mantendo tudo organizado e limpo.

Para instala-lo é bem simples, abra um terminal (o prompt de comando) e navegue até a pasta que deseja iniciar o VEnv, quando já estiver nela execute os seguintes comandos:

`python -m pip install virtualenv` (aguarde a conclusão)

`python -m virtualenv .venv` (aguarde a conclusão)

após isso, você poderá ativar o VEnv, a forma muda dependendo do terminal usado (PowerShell ou CMD), basta executar uma das seguintes linhas:
- CMD: `.venv\Scripts\activate.bat`
- PowerShell: `.venv\bin\Activate.ps1`

Se tudo ocorrer bem, você deverá ver um `(.venv)` no início do seu prompt.

#### Instalando o Python no Linux (ou Sistemas UNIX)

Basta seguir as instruções do seu gerenciador de pacotes e instalar a versão mais recente do Python (ou uma superior ou igual a 3.10).

Caso não exista, você deverá compilar pelo código fonte.

As instruções para sistemas baseados em Debian (Ubuntu, ZorinOS, etc...) são as seguintes (se seu sitema não for baseado em Debian, sugiro pesquisar na internet como fazer o mesmo):
- Abra um terminal
- Instale os pacotes necessários para build usando o seguinte comando:
    - ```sudo apt install wget build-essential libreadline-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev```
- Baixe a Tarball usando `wget`:
    - ```wget -c https://www.python.org/ftp/python/3.11.0/Python-3.11.0.tar.xz```
    - Nesse caso, estaremos baixando a tarball da versão 3.11, para futuras versões basta trocar o numero da versão na URL.
- extraia a tarball e navegue para o diretório:
    - ```tar -Jxf Python-3.11.0.tar.xz```
    - ```cd Python-3.11.0/```
- Otimize, compile e instale:
    - ```./configure --enable-optimizations```
    - ```make -j4 && sudo make altinstall```
        - o numero ao lado do `j` especifica a quantidade de threads usadas para compilação, se você tiver um processador com mais threads e quiser acelerar o processo sinta-se livre para aumentar esse numero.
- Cheque a instalação, para isso basta ver se tudo foi instalado corretamente com os seguintes comandos:
    - ```python3.11 --version```
    - ```python3.11 -m pip --version```

Não há necessidade de instalar um executável a parte para o terminal, pois em sistemas UNIX o interpretador já funciona no terminal.

O ambiente virtual é uma espécie de container para o seu código, separando cada projeto do seu sistema, mantendo tudo organizado e limpo.

Para instala-lo é bem simples, abra um terminal (o prompt de comando) e navegue até a pasta que deseja iniciar o VEnv, quando já estiver nela execute os seguintes comandos:

`python3.11 -m pip install virtualenv` (aguarde a conclusão)

`python3.11 -m virtualenv .venv` (aguarde a conclusão)

após isso, você poderá ativar o VEnv, basta executar o seguinte comando:

`source .venv/bin/activate`

Se tudo ocorrer bem, você deverá ver um `(.venv)` no início do seu prompt.

### Configurando a IDE (Visual Studio Code)

Uma IDE (Integrated Development Environment) ou Ambiênte de Desenvolvimento Integrado, é um programa desenvolvido para auxiliar no desenvolvimento de aplicações, extendendo as funcionalidades de um simples editor de texto.

Nesse curso eu costumo utilizar o Visual Studio Code (VSCode), você pode baixa-lo através [desse link](https://code.visualstudio.com/Download), mas também existem outras IDEs como o [Pycharm](https://www.jetbrains.com/pycharm/), [NeoVIM](https://neovim.io/); e também nada o impede de digitar código no [NotePad++](https://notepad-plus-plus.org/), ou até mesmo no bloco de notas padrão do Windows.

Após a instalação do VSCode navegue para a aba de extensões na barra lateral, e instale a extensão do Python, existem diversos tutoriais na internet sobre o VSCode, sinta-se livre para pesquisar e se tornar confortavel com a IDE.

## Capitulos Escritos (Roadmap)

- [ ] 00. Python Lessons \[O Curso todo num arquivo só\]
- [x] 01. Introdução a Programação
- [x] 02. Fundamentos do Python - I
- [x] 03. Fundamentos do Python - II
- [x] 04. Programação Orientada a Objetos
- [ ] 05. Erros \[EM PROGRESSO\]
- [ ] 06. Arquivos
- [ ] 07. Databases
- [ ] 08. Type-Hint
- [ ] 09. Funções nativas avançadas
- [ ] 10. Desenvolvimento avançado
- [ ] 11. Web Scraping
- [ ] 12. Automação de navegador com Selenium
- [ ] 13. Async Dev
- [ ] 14. Virtualização
- [ ] 15. Webdev Flask
- [ ] 16. APIs
- [ ] 17. Decoradores
- [ ] 18. Programação Orientada a Objetos Avançada
- [ ] 19. Desenvolvimento de GUI com Tkinter
- [ ] 20. Desenvolvimento de Interfaces Graficas
- [ ] 21. Desenvolvimento Mobile
- [ ] 22. Unit Tests
- [ ] 23. Ciencia de Dados
- [ ] 24. Algoritmos, Estrutura de Dados e Machine Learning
- [ ] 25. Bibliotecas
- [ ] 26. Documentação e Boas Praticas
- [ ] 27. Redes e Soquetes
- [ ] 28. Criptografia
- [ ] 29. Cyber Segurança e Hacking Ético
- [ ] 30. Noções Avançadas de Programação
- [ ] 31. Game Dev
