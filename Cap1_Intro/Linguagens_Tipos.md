# Linguagens de programação e suas classificações

Linguagens de programação são uma serie de instruções dadas em à maquina em um arquivo comumente conhecido como _"Código Fonte"_, elas possibilitam que o programador/engenheiro de software, transcreva suas  ideias para a linguagem de maquina, criando assim o que chamamos de "software" ou "programa computacional".

_De acordo com a Wikipédia:_

> *"A linguagem de programação é um método padronizado, formado por um conjunto de regras sintáticas e semânticas, de implementação de um código fonte - que pode ser compilado e transformado em um programa de computador, ou usado como script interpretado - que informará instruções de processamento ao computador. Permite que um programador especifique precisamente quais os dados que o computador irá atuar, como estes dados serão armazenados ou transmitidos e, quais ações devem ser tomadas de acordo com as circunstâncias. Linguagens de programação podem ser usadas para expressar algoritmos com precisão."*
> 
> _(...)_
> 
> *"Uma das principais metas das linguagens de programação é que programadores tenham uma maior produtividade, permitindo expressar suas intenções mais facilmente do que quando comparado com a linguagem que um computador entende nativamente (código de máquina). Assim, linguagens de programação são projetadas para adotar uma sintaxe de nível mais alto, que pode ser mais facilmente entendida por programadores humanos. Linguagens de programação são ferramentas importantes para que programadores e engenheiros de software possam escrever programas mais organizados e com maior rapidez."*

As linguagens podem ser classificadas de acordo com seus paradigmas, método de tradução, tipagem, nível, geração, entre outros, vale também ressaltar que uma linguagem pode ter mais de um tipo de classificação dentro de um mesmo campo.

Uma pequena introdução aos conceitos mais comuns:

- Linguagens Matriz: A matriz de uma linguagem define sua utilidade principal, são 3 tipos, Programação (Logica), Marcação (Documentação), Estilo (Design)
  
  - Programação (Logica): As linguagens de Programação são marcadas por funções e comandos, elas trabalham a logica de maquina, alguns exemplos são, Python e BASH.
  
  - Marcação (Documentação): As Linguagens de Marcação são marcada pelo uso de marcadores de texto (ex: itálico, negrito, cabeçalhos, etc...), elas são mais usadas na criação de documentos, exemplos seriam MarkDown e HTML (HyperTextMarkupLanguage)
  
  - Estilo (Design): As Linguagens de Estilo são marcadas pelo o uso de propriedades de aparência (ex: background-color, shadow, etc...), elas são usadas na estilização de sites e aplicativos, exemplos seriam CSS e SASS

-  Paradigma:
  
  - O paradigma de uma linguagem de programação define sua funcionalidade, especificidade, ou orientação, informalmente dizendo, o paradigma de uma linguagem é o equivalente a "uma serie de métodos, dogmas, regras e conceitos que guiam o código fonte"
  
  - os 3 paradigmas mais comuns são:
    
    - Imperativa: as etapas são sequenciadas, normalmente de cima abaixo, e os comandos são imperativos, informalmente falando, são ordem que devem ser estritamente seguidas. Linguagens de *scripting* são os melhores exemplos para se descrever Imperatividade, um exemplo com a linguagem BASH:
      
      - ```shell
        str="Movendo Arquivo1"            # Primeira Instrução
        printf "%s\n" "${str}"            # Segunda Instrução
        mv -vi Arquivo1.ext /diretorio1/  # Terceira Instrução
        printf "%s\n" "Concluido"         # Quarta Instrução 
        ```
    
    - Funcional: as etapas são divididas em blocos de código chamados funções e são executados de acordo com a sua chamada, ou seja, se a função X foi declarada na linha 38 de um programa e a função Y foi declarada na linha 85, sua execução independe da sequencia de declaração (é claro que, as funções não devem ser chamadas antes de suas devidas declarações), resultando em nós podendo chamar a função Y na linha 102 e função X na linha 103, um exemplo seria a linguagem de programação Go:
      
      - ```go
        package main
        
        import "fmt"
        
        // Aqui nós declaramos a primeira função
        func funcao_print_1() {
            fmt.Println("Função 1")
        }
        
        // Aqui nós declaramos a segunda função
        func funcao_print_2() {
            fmt.Println("Função 2")
        } 
        
        func main() {
            funcao_print_2() // Aqui chamamos a segunda
            funcao_print_1()  // Aqui chamamos a primeira
        }
        ```
        
        Note a ordem de declaração e de chamada, declaramos a `funcao_print_1` primeiro, e depois a `funcao_print_2`, porém chamamos a `funcao_print_2` antes da `funcao_print_1`
    
    - Orientada a Objetos: este paradigma segue a interpretação de que os códigos devem ser divididos em objetos (classes), objetos são pequenos contêineres independentes entre si, a orientação a objetos é um campo de estudo deverás complexo, alguns dos seus conceitos como a [Abstração](https://pt.wikipedia.org/wiki/Abstração_(ciência_da_computação)) e a [Ação nos objetos](https://pt.wikipedia.org/wiki/Orientação_a_objetos#Ação_nos_objetos) costumam sempre confundir, você se percebem falando coisas como "o que é um cachorro?", "uma mensagem deveria se auto-mandar, ou ela deveria ser mandada por outra coisa?" e por ai vai. Alguns dos conceitos tratados pela orientação a objeto foram incorporados em outros paradigmas, como as classes. Uma das linguagens orientadas a objetos mais famosas é a Java, aqui um exemplo de código:
      
      - ```java
        public class Program {
            public static void main(String[] args) throws Exception {
                String str = "Olá Mundo";
                System.out.println(str);
            }
        }
        ```

- Tipagem: ela define a estrutura de tipos, ela essencialmente define a "praticidade" e o "controle" que o programador tem com a linguagem de programação
  
  - Força: Define a volatilidade da variável na memória, pode ser divida em Fraca ou Forte:
    
    - Fraca: Linguagens Fracamente Tipadas tem o tipo de suas variáveis mudadas na memória de acordo com a situação
    
    - Forte: Linguagens Fortemente Tipadas tem seu tipo mantido na memória, uma vez que o mesmo já foi atribuído
  
  - Estilo: Define a imperatividade da variável, pode ser divido em Estático e Dinâmico:
    
    - Estático: Linguagens Estaticamente Tipadas, tem o tipo de suas variáveis definido em tempo de compilação, uma diferença nítida é o tipo da variável sendo especificado no código fonte (vide Java)
    
    - Dinâmico: Linguagens Dinamicamente Tipoadas, tem o tipo de suas variáveis definido em tempo de execução, uma diferença seria o tipo da variável sendo omitida no código fonte (vide Python)
      
      - Exemplo de Estilo:
      
      - ```
        string texto = "Esse aqui é um texto" # Linguagens Estaticas
        texto = "Esse aqui é um texto"        # Linguagens Dinâmicas
        ```

- Nível: o nível de uma linguagem de programação define sua "humanidade" e "completude", basicamente, quanto mais alto o nível, mais perto da linguagem humana o código fonte é, e mais funções e coisas a linguagem faz de forma "automática", elas podem ser dividas em Baixo e Alto nível
  
  - Linguagens de Baixo Nível: As linguagens de baixo nível são extremamente próximas do código de maquina (também conhecido como binário), uma das linguagens de mais baixo nível ainda em uso seria a linguagem Assembly, ela trabalha movendo bits para registradores e locais diretos na memoria, um código executado direto no processador, eis aqui um programa que exibe a mensagem "Olá Mundo":
    
    - ```nasm
      section .data
          str db "Olá Mundo!", 0xA ; Declara a variavel str="Olá Mundo!" e adiciona o LineFeed
          len equ $ - str          ; Coleta o tamanho em bits da variavel
      
      global _start
      section .text
      _start:
          mov eax, 4              ; Usa o código de operação do kernel SYS_WRITE
          mov ebx, 1              ; Usa o StdIO, nesse caso, usaremos o StdIn
          mov ecx, str            ; Move a variavel str para parametro const_char
          mov edx, len            ; Move o tamanho em bits da variavel para o parametro size_t
          int 0x80                ; Chama o kernel para performar a operação
      
          mov eax, 1              ; Usa o código de operação do kernel SYS_EXIT
          int 0x80                ; Chama o kernel para performar a operação
      ```
  
  - Linguagens de Alto Nível: As linguagens de Alto Nível são bem próximas da linguagem humana, e as linguagens acabam por fazer muitas tarefas simples por nós em segundo plano, coisas como limpar a memória em uso, mover os bits para os registradores, entre outras coisas, Linguagens de Alto Nível são amplamente usadas devido a sua praticidade e facilidade de aprendizado e uso, eis aqui um exemplo de programa em Python que exibe a mensagem "Olá Mundo!":
    
    - ```python
      print("Olá Mundo!")
      ```

Essas classificações simplificam nossa compreensão das linguagens
