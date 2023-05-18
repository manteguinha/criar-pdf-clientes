# Documentação: Programa de criar PDFs

Este programa é uma aplicação de desktop que usa a biblioteca PySimpleGUI para a interface gráfica e a biblioteca reportlab para a criação de arquivos PDF. A aplicação permite aos usuários criar e personalizar PDFs com informações pessoais, planos de internet e opções de roteador.

## Requisitos

Antes de começar a executar o programa, instale as seguintes bibliotecas:

```
pip install PySimpleGUI
pip install reportlab
pip install unidecode
```

## Estrutura do Código

O código é estruturado em uma classe chamada `PDF`, que possui três métodos principais:

1. `__init__()`: construtor da classe, responsável por criar a janela do aplicativo e seus elementos.
2. `iniciar()`: método que inicia o loop de eventos do aplicativo e aguarda ações do usuário.
3. `criarPDF()`: método que cria o arquivo PDF com base nos valores fornecidos pelo usuário.

### Classe PDF

A classe `PDF` é responsável por criar a interface gráfica do aplicativo e gerenciar os eventos e valores dos campos de entrada.

#### Método `__init__()`

Este método cria a janela e define o layout do aplicativo. Os elementos da janela incluem:

- Campos de entrada para Nome, CPF, Telefone, Endereço, Setor, CEP, Cidade e Observações.
- Opções de rádio para Sobrado e Roteador.
- Um menu suspenso para escolher o plano de internet.
- Um botão para anexar arquivos de imagem.
- Um botão para criar o arquivo PDF.

#### Método `iniciar()`

Este método inicia o loop de eventos do aplicativo e aguarda ações do usuário. O loop termina quando a janela é fechada ou quando o botão "Criar PDF" é pressionado, chamando o método `criarPDF()`.

#### Método `criarPDF()`

Este método cria o arquivo PDF com base nos valores fornecidos pelo usuário nos campos de entrada. Ele verifica se os campos obrigatórios estão preenchidos antes de criar o arquivo PDF. Se algum campo obrigatório estiver vazio, uma mensagem de erro será exibida.

O método `criarPDF()` também ajusta o valor do plano de internet e do roteador com base nas opções selecionadas pelo usuário e adiciona uma imagem ao PDF, se fornecida.

## Execução do Programa

Para executar o programa, instale as dependências mencionadas acima e execute o arquivo Python:

```bash
python app.py
```

Preencha os campos obrigatórios e clique no botão "Criar PDF" para gerar o arquivo PDF. O arquivo será salvo no diretório atual com o nome do cliente como nome do arquivo.
