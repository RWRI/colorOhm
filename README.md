<div align="center">
    <img src="./logo.png" alt="Logo" width="150">
    <h1>Linguagem ColorOhm</h1>
</div>

<details>
  <summary>Sumário</summary>
  <ol>
    <li>
      <a href="#sobre-o-projeto">Sobre o projeto</a>
      <ul>
        <li><a href="#tecnologias">Tecnologias</a></li>
      </ul>
    </li>
    <li>
      <a href="#introdução">Introdução</a>
      <ul>
        <li><a href="#instalação">Instalação</a></li>
        <li><a href="#como-rodar">Como rodar</a></li>
      </ul>
    </li>
    <li><a href="#desenvolvimento">Desenvolvimento</a></li>
  </ol>
</details>

## Sobre o projeto

Essa linguagem foi construída para a disciplina de Compiladores da Universidade Federal de Itajubá. Ela visa a transformação de um valor para o código de cores de um resistor ou o contrário.

As operações são feitas utilizando o seguinte modelo:

![Código de cores resistor](https://embarcados.com.br/wp-content/uploads/2022/05/image-31.png)

### Tecnologias

Para construir essa linguagem foi utilizado da linguagem pyton.

* ![[Python][Python]][Python-url]]

[Python]: https://www.python.org/static/img/python-logo@2x.png
[Python-url]: https://www.python.org/

## Introdução

Nesta seção será apresentado como instalar todos os itens necessários e como utilizar o programa.

### Instalação

<details>
    <summary>Como instalar o Python no Windows</summary>
    
A instalação do Python no Windows segue o padrão da maioria dos programas instalados no sistema operacional em questão com uma única ressalva: no início do processo de instalação, deve-se selecionar a opção “Add Python (version) to PATH”. Com isso, o Windows saberá onde está localizado o interpretador do Python e, assim, conseguiremos utilizá-lo sem problemas.

1. Acesse a [página oficial](https://www.python.org/downloads/) para realizar o download do instalador do Python na versão desejada
2. Vá até a pasta na qual foi feito o download do instalador do Python
3. Clique com o botão direito em cima do instalador e clique na opção “Executar como Administrador”.
4. Com o instalador aberto tenha a certeza de ter marcado as opções “Add Python (version) to PATH” para que o comando python fique disponível.
5. Por fim clique em “Install Now” e siga o processo padrão de instalação de programas no Windows (next, next, next, finish).
</details>

<details>
    <summary>Como instalar o Python no Linux</summary>
    
Os sistemas GNU/Linux mais recentes ja possuem uma versão do Python instalada junto com o sistema operacional. Podemos checar com o seguinte comando:

`which python3`

* Debian e Ubuntu: Através do gerenciador de pacotes, é possível instalar versões específicas do Python. No exemplo abaixo, é instalada a versão, por exemplo, 3.9 do Python.

    `sudo apt-get install python3.9`
* RedHat e CentOS: Assim como no tópico anterior, é possível instalar versões específicas do Python. No comando abaixo, é instalada a versão, por exemplo, 3.9 do Python.

    `sudo yum install python3.9`

</details>

### Como rodar



## Desenvolvimento

Esse projeto foi desenvolvido por:

* Bárbara Alves de Paiva Barbosa - [@barbaralves](https://github.com/barbaralves) - barbara.pb.alves@gmail.com